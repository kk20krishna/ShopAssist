from functions import *

'''
if __name__ == "__main__":
    
    for i in range(1, 6):
        print(f"Test {i}:")
        try:
            # Assuming get_configs is a function that retrieves configurations
            op = get_configs('conversation', 'model')
            print(op)
        except Exception as e:
            print(f"An error occurred: {e}")
        print("-" * 20)
#     # Test the get_configs function
'''

from dotenv import load_dotenv
import os

load_dotenv()
print("OPENAI_API_KEY: ", os.getenv('OPENAI_API_KEY'))

from openai import OpenAI

client = OpenAI()


response = client.responses.create(
    model="gpt-3.5-turbo",
    input=[
          {"role": "user", "content": "Recomend me a laptop for gaming. Go with your assumptions."}
        ],
    #tools=[function_recommend_laptops]
)

print(response.output_text)