# Import necessary libraries
from flask import Flask, redirect, url_for, render_template, request
from functions import *
from dotenv import load_dotenv

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

@app.route("/")
def default_func():
    global conversation, conversation_bot
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

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')