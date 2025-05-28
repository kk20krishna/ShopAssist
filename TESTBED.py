from functions import *
import openai
import ast
import re
import pandas as pd
import json
from IPython.display import display, HTML
import yaml
from functools import lru_cache
from openai import OpenAI

import json

args = {'budget': 15, 'Portability': 'high', 'GPU intensity': 'high', 'Multitasking': 'high', 'Display quality': 'high', 'Processing speed': 'high'}

def recommend_laptops(**args):
    #print('recommend_laptops called with args:', args)
    laptop_df = pd.read_csv('updated_laptop.csv')

    budget = args.get('budget')

    filtered_laptops = laptop_df.copy()
    filtered_laptops['Price'] = filtered_laptops['Price'].str.replace(',', '').astype(int)
    filtered_laptops = filtered_laptops[filtered_laptops['Price'] <= budget].copy()

    # # # Mapping string values 'low', 'medium', 'high' to numerical scores 0, 1, 2
    mappings = {'low': 0, 'medium': 1, 'high': 2}

    # # # Creating a new column 'Score' in the filtered DataFrame and initializing it to 0
    filtered_laptops['Score'] = 0

    #print('forS start now')
    # # # Iterating over each laptop in the filtered DataFrame to calculate scores based on user requirements
    for index, row in filtered_laptops.iterrows():
        print('Outer for:', index, row['laptop_feature'])
        laptop_config_str = row['laptop_feature']
        laptop_config_str = laptop_config_str.replace("'", '"')  # Replacing single quotes with double quotes for valid JSON
        laptop_config = json.loads(laptop_config_str)
        #print('laptop_config:', laptop_config)
        score = 0

    #   # Comparing user requirements with laptop features and updating scores
        for user_req_key, user_req_value in args.items():
            #print('Inner for:', user_req_key, user_req_value)
            if user_req_key == 'budget':
                continue  # Skipping budget comparison
            
            #print(mappings.get(laptop_config.get(user_req_key, None), -1), mappings.get(user_req_value, -1))

            if mappings.get(laptop_config.get(user_req_key, None), -1) >= mappings.get(user_req_value, -1):
                score += 1  # Incrementing score if laptop value meets or exceeds user value
            
            #print('score:', score)

        filtered_laptops.loc[index, 'Score'] = score  # Updating the 'Score' column in the DataFrame


    # Sorting laptops by score in descending order and selecting the top 3 products
    top_laptops = filtered_laptops.drop('laptop_feature', axis=1)
    top_laptops = top_laptops[top_laptops['Score'] > 2]  # Filtering out laptops with a score of 2 or more
    top_laptops = top_laptops.sort_values('Score', ascending=False).head(3) # select top 3 laptops based on score
    top_laptops_json = top_laptops.to_json(orient='records')  # Converting the top laptops DataFrame to JSON format

    # top_laptops
    return top_laptops_json


print(recommend_laptops(**args))