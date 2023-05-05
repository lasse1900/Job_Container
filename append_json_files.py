import json

# TODO get the number of files as an argument
def parse_json_files_together():

    with open("input_0.json", encoding='utf-8') as json_file:
        data = json.load(json_file)

    with open("input_1.json", encoding='utf-8') as json_file:
        data2 = json.load(json_file)
        temp = data
        temp.extend(data2)
