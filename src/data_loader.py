import json
from pathlib import Path

def read_file(path_file: Path)->dict:
    with path_file.open("r") as f:
        file = json.load(f)
        return file

