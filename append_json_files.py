import json

def write_json(data, filename="output.json"):
    with open(filename, "w", encoding='utf-8') as file:
        json.dump(data, file, indent=4)

with open("input_1.json", encoding='utf-8') as json_file:
    data = json.load(json_file)
with open("input_2.json", encoding='utf-8') as json_file:
    data2 = json.load(json_file)
    temp = data
    temp.extend(data2)

write_json(data)