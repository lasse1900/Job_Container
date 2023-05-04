import json

# TODO get the number of files as an argument
def parse_json_files_together():

    def write_json(data, filename="output.json"):
        with open(filename, "w", encoding='utf-8') as file:
            json.dump(data, file, indent=4)

    with open("input_0.json", encoding='utf-8') as json_file:
        data = json.load(json_file)

    with open("input_1.json", encoding='utf-8') as json_file:
        data2 = json.load(json_file)
        temp = data
        temp.extend(data2)

    with open("input_2.json", encoding='utf-8') as json_file:
        data3 = json.load(json_file)
        temp = data
        temp.extend(data3)

    with open("input_3.json", encoding='utf-8') as json_file:
        data4 = json.load(json_file)
        temp = data
        temp.extend(data4)

    write_json(data)