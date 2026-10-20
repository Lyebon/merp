import json

def read_file(path_file: str)->dict:
    with open(path_file, "r") as f:
        file = json.load(f)
        return file

