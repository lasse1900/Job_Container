import json
import pypandoc

# Formating JSON as MD to docx
# Skandic alphabeths fail
# pandoc formated.md -f markdown -t docx -o example.docx (command line)

with open('sorted.json', 'r') as file:
    data = file.read()

# sparate call to read line count
with open("sorted.json", 'r') as fp:
    for count, line in enumerate(fp):
        pass
print('Total Lines', count + 1)

number_of_jobs = (count - 2)/16
print(f'Number of jobs: {int(number_of_jobs)}')
top = int(number_of_jobs)-1

with open("formated.md", "w") as wf:
    for i in range(top):
        content = json.loads(data)[i]
        print(content)

        def format(key, value):
            return f"<{value}>" if key.endswith("_url") else value

        for key, value in content.items():
            wf.write(f"- {key} : {format(key, value)}")

input_file = "formated.md"
output_file = "output2.docx"

output = pypandoc.convert_file(input_file, "docx", outputfile=output_file)