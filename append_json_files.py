import json
import pathlib
import itertools
import os
# TODO get the number of files as an argument
file_paths = [
    'input_0.json',
    'input_1.json',
    'input_2.json',
    'input_3.json'
]

error = False
# Check existence of each file
# TODO add this to method chechs OR TRY / CATCH
for file_path in file_paths:
    if os.path.exists(file_path):
        print(f"{file_path} exists")
    else:
        print(f"{file_path} does not exist")
        error = True

if(error != True):
    print("All needed input files found, let's go on")
else:
    print("Input files missing in append_json_files.py")
    
def parse_json_files_together():
    # file_paths = ["input_0.json", "input_1.json"]        
    file_paths = ["input_0.json", "input_1.json", "input_2.json", "input_3.json"]
    input_data = [json.loads(pathlib.Path(f).read_text(encoding="utf-8")) for f in file_paths]
    output_data = list(itertools.chain(*input_data))
    pathlib.Path("output_temp.json").write_text(json.dumps(output_data), encoding="utf-8")

    with open('output.json', 'w', encoding='utf-8') as f:
        json.dump(output_data, f, ensure_ascii=False, indent=4)
