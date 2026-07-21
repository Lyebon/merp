import json

def read_file(file:dict[str:dict])->dict:
    with open(file) as f:
        file = json.load(f)