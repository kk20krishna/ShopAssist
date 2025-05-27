import yaml

print("Loading init_conversation.yaml file...")
with open("init_conversation.yaml", "r") as file:
    YAML_DICT = yaml.safe_load(file)
    print(YAML_DICT['messages'])
    print("init_conversation.yaml file loaded successfully.")