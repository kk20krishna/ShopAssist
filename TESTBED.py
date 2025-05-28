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

args = {'budget': 1500, 'portability': 'high', 'gpuIntensity': 'high', 'multitasking': 'high', 'displayQuality': 'high', 'processingSpeed': 'high'}

def recommend_laptops(**args):
    laptop_df = pd.read_csv('updated_laptop.csv')

    budget = args.get('budget')
    portability = args.get('portability')
    gpu_intensity = args.get('gpuIntensity')
    multitasking = args.get('multitasking')
    display_quality = args.get('displayQuality')
    processing_speed = args.get('processingSpeed')

    filtered_laptops = laptop_df.copy()
    filtered_laptops['Price'] = filtered_laptops['Price'].str.replace(',', '').astype(int)
    filtered_laptops = filtered_laptops[filtered_laptops['Price'] <= budget].copy()

    # # # Mapping string values 'low', 'medium', 'high' to numerical scores 0, 1, 2
    mappings = {'low': 0, 'medium': 1, 'high': 2}

    # # # Creating a new column 'Score' in the filtered DataFrame and initializing it to 0
    filtered_laptops['Score'] = 0

    # # # Iterating over each laptop in the filtered DataFrame to calculate scores based on user requirements
    for index, row in filtered_laptops.iterrows():
        user_product_match_str = row['laptop_feature']
        laptop_values = user_product_match_str
        laptop_values = dictionary_present(user_product_match_str)
        score = 0

    #     # Comparing user requirements with laptop features and updating scores
        for key, user_value in user_requirements.items():
            # if key.lower() == 'budget':
            if key == 'Budget':
                continue  # Skipping budget comparison
            laptop_value = laptop_values.get(key, None)
            # print(key, laptop_value)
            laptop_mapping = mappings.get(laptop_value, -1)
            # laptop_mapping = mappings.get(laptop_value, -1)
            # user_mapping = mappings.get(user_value, -1)
            user_mapping = mappings.get(user_value, -1)
            if laptop_mapping >= user_mapping:
                score += 1  # Incrementing score if laptop value meets or exceeds user value

        filtered_laptops.loc[index, 'Score'] = score  # Updating the 'Score' column in the DataFrame

    # Sorting laptops by score in descending order and selecting the top 3 products
    top_laptops = filtered_laptops.drop('laptop_feature', axis=1)
    top_laptops = top_laptops.sort_values('Score', ascending=False).head(3)
    top_laptops_json = top_laptops.to_json(orient='records')  # Converting the top laptops DataFrame to JSON format

    # top_laptops
    return top_laptops_json