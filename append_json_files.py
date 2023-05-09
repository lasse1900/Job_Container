import json
import pathlib
import itertools
    
def parse_json_files_together(row_count):
    file_paths = []  # create an empty list for the needed filenames
    # add more filenames to the list according to keywords row count
    for i in range(row_count):
        file_paths.append(f"input_{i}.json")
    print(f"file_paths {file_paths}")  
    input_data = [json.loads(pathlib.Path(f).read_text(encoding="utf-8")) for f in file_paths]
    output_data = list(itertools.chain(*input_data))
    pathlib.Path("output_temp.json").write_text(json.dumps(output_data), encoding="utf-8")

    print(f"------------>>> input_{i}.json")

    with open(f"input_{i}.json", 'w', encoding='utf-8') as f:
        json.dump(output_data, f, ensure_ascii=False, indent=4)
