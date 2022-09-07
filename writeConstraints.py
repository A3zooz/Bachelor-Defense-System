import json
def load_data(path):
    with open(path, 'r') as read_file:
        data = json.load(read_file)
        