import openai
import ast
import re
import pandas as pd
import json
from IPython.display import display, HTML
from flask import Flask, redirect, url_for, render_template, request
from functions import *
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

conversation = []
conversation_bot = []

# Append system prompt to the conversation
conversation_bot.append({'role' : 'system', 'content': get_configs('conversation', 'system_prompt')})

# Append assistant greeting to the conversation
assistant_greeting = get_configs('conversation', 'assistant_greeting')
conversation_bot.append({'role': 'assistant', 'content': assistant_greeting})
conversation.append({'role': 'assistant', 'content': assistant_greeting})

# Append TEST_INT_CONVERSATION to the conversation ####
for item in test_int_conversaion():
    conversation_bot.append(item)
    conversation.append(item)
#######################################################

top_3_laptops = None

@app.route("/")
def default_func():
    global conversation, conversation_bot, top_3_laptops
    return render_template("shopAssist.html", conversation = conversation)

@app.route("/chat", methods = ['POST'])
def chat():
    global conversation, conversation_bot
    user_input = request.form["user_input"]
    
    # Perform moderation check on user input
    moderation = moderation_check(user_input)
    if moderation == 'Flagged':
        conversation.append({'role': 'moderation', 'content': get_configs('conversation', 'moderation_message_user')})
        return redirect(url_for('default_func'))

    conversation_bot.append({'role': 'user', 'content': user_input})
    conversation.append({'role': 'user', 'content': user_input})

    # Get chat completions from the model
    assistant_output = get_chat_completions(conversation_bot)

    # Perform moderation check on assistant output
    moderation = moderation_check(assistant_output)
    if moderation == 'Flagged':
        conversation.append({'role': 'moderation', 'content': get_configs('conversation', 'moderation_message_assistant')})
        return redirect(url_for('default_func'))

    conversation_bot.append({'role': 'assistant', 'content': assistant_output})
    conversation.append({'role': 'assistant', 'content': assistant_output}) 
    return redirect(url_for('default_func'))


@app.route("/end_chat", methods = ['POST'])
def end_conv():
    global conversation_bot, conversation
    conversation = []
    conversation_bot = []
    conversation_bot.append({'role' : 'system', 'content': get_configs('conversation', 'system_prompt')})
    assistant_greeting = get_configs('conversation', 'assistant_greeting')
    conversation_bot.append({'role': 'assistant', 'content': assistant_greeting})
    conversation.append({'role': 'assistant', 'content': assistant_greeting})
    return redirect(url_for('default_func'))

'''
@app.route("/invite", methods = ['POST'])
def invite():
    global conversation_bot, conversation, top_3_laptops, conversation_reco
    user_input = request.form["user_input_message"]
    prompt = 'Remember that you are a intelligent laptop shopping assistant. You should help and answer only with the queries related to laptops. If the queries are not related to laptops, just say something like you can help only with queries related to laptops etc.'
    moderation = moderation_check(user_input)
    if moderation == 'Flagged':
        display("Sorry, this message has been flagged. Please restart your conversation.")
        return redirect(url_for('end_conv'))
    
    if top_3_laptops is None:

        conversation.append({"role": "user", "content": user_input + prompt})
        conversation_bot.append({'user': user_input})

        response_assistant = get_chat_completions(conversation)
        moderation = moderation_check(response_assistant)
        if moderation == 'Flagged':
            display("Sorry, this message has been flagged. Please restart your conversation.")
            return redirect(url_for('end_conv'))    


        confirmation = intent_confirmation_layer(response_assistant)

        print("Intent Confirmation Yes/No:",confirmation.get('result'))

        if "No" in confirmation.get('result'):
            conversation.append({"role": "assistant", "content": str(response_assistant)})
            conversation_bot.append({'bot': response_assistant})

        else:
            response = dictionary_present(response_assistant)
            print("WAIT")
            conversation_bot.append({'bot': "Thank you for providing all the information. Kindly wait, while I fetch the products: \n"})

            top_3_laptops = compare_laptops_with_user(response)

            print("top 3 laptops are", top_3_laptops)

            validated_reco = recommendation_validation(top_3_laptops)
            if len(validated_reco) == 0:
                conversation_bot.append({'bot': "Sorry, we do not have laptops that match your requirements."})

            conversation_reco = initialize_conv_reco(validated_reco)
            conversation_reco.append({"role": "user", "content": "This is my user profile" + str(validated_reco)})
            recommendation = get_chat_completions(conversation_reco)

            moderation = moderation_check(recommendation)
            if moderation == 'Flagged':
                display("Sorry, this message has been flagged. Please restart your conversation.")
                return redirect(url_for('end_conv'))

            conversation_reco.append({"role": "assistant", "content": str(recommendation)})
            conversation_bot.append({'bot': recommendation})

    else:
        conversation_reco.append({"role": "user", "content": user_input})
        conversation_bot.append({'user': user_input})

        response_asst_reco = get_chat_completions(conversation_reco)

        moderation = moderation_check(response_asst_reco)
        if moderation == 'Flagged':
            print("Sorry, this message has been flagged. Please restart your conversation.")
            return redirect(url_for('end_conv'))

        conversation.append({"role": "assistant", "content": response_asst_reco})
        conversation_bot.append({'bot': response_asst_reco})

    return redirect(url_for('default_func'))
'''

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

    