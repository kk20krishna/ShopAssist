from functions import *


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
