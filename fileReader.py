import json

def read_file(file_name):
    with open('stocks.json') as json_file:
        json_data = json.load(json_file)
        return json_data
