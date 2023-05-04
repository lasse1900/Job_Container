import json
import pypandoc

# Formating JSON as MD to docx
# pandoc formated.md -f markdown -t docx -o example.docx (on command line)

input_file = "formated.md"
output_file = "jobs.docx"

def format_2_docx():
    with open('sorted.json', 'r') as file:
        data = file.read()

    # sparate call to read line count
    with open("sorted.json", 'r', encoding="utf-8") as fp:
        for count, line in enumerate(fp):
            pass
    # print('Total Lines', count + 1)

    number_of_jobs = (count - 2)/17
    print(f'Number of jobs: {int(number_of_jobs)}')
    top = int(number_of_jobs)-1

    desired_keys = ["company_name", "date", "job_location", "job_title", "job_url"]

    with open("formated.md", "w") as wf:
        wf.write("OPEN JOBS on <fi.indeed.com>")
        wf.write("\n")
        wf.write("-"*25)
        wf.write("\n")
        def format(key, value):
            return f"<{value}>" if key.endswith("_url") else value
        
        for i in range(top):
            content = json.loads(data)[i]

            # Printed only desired fields added with CR
            for key, value in content.items():
                if key in desired_keys:
                    wf.write(f"{key} : {format(key, value)}\n")
                    wf.write("\n")
            # Add separator after each object
            wf.write("-"*25)
            wf.write("\n")
            wf.write("\n")


        output = pypandoc.convert_file(input_file, "docx", outputfile=output_file)