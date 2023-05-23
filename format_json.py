import json
import csv
import pypandoc
import pandas
import math
from datetime import datetime as dt
today = dt.today()

# Formating JSON as MD to docx
# pandoc formated.md -f markdown -t docx -o example.docx (on command line)

input_file = "formated.md"
output_file = "jobs.docx"

# reading search terms from csv file
file_params = pandas.read_csv('search_terms.csv')
keywords = []
locations = []
for index, row in file_params.iterrows():
    sana = row['keyword']
    location = row['location']
    keywords.append(sana)
    locations.append(location)

subject = "Open Jobs on Indeed - " + today.strftime("%B %d, %Y")

# In case locations are missing and default location 'Suomi' is added into list    
csv_file = "locations_bup.csv"
locations_updated = ""
# Open the CSV file in read mode
with open(csv_file, mode='r') as file:
    reader = csv.reader(file)
    # Iterate over each row in the CSV file
    for row in reader:
        # Join the values of each row into a string
        row_string = ','.join(row)
        locations_updated += row_string
# print("Pypandoc: ", locations_updated)

# Input to this Pandoc formating is filtered.json file, which is converted through markdown to docx
def format_2_docx():
    with open('filtered.json', 'r') as file:
        data = file.read()

    # sparate call to read line count
    with open("filtered.json", 'r', encoding="utf-8") as fp:
        for count, line in enumerate(fp):
            pass
    # print('Total Lines', count + 1)

    number_of_jobs = (count - 2)/17
    jobs = math.floor(number_of_jobs)
    # print(f'Number of jobs = [filtered.json lines/17]: {jobs}')
    top = jobs

    desired_keys = ["company_name", "date", "job_location", "job_title", "job_url"]
    key = "https://fi.indeed.com"

    with open("formated.md", "w") as wf:
        def format_one_link(key):
            return f"<{key}>"
        wf.write(f"Open jobs at:  {format_one_link(key)}\n  Date: " + today.strftime("%B %d, %Y"))
        wf.write("\n")
        wf.write("\n")
        wf.write(f" At locations {locations_updated} {jobs} open jobs")        
        wf.write("\n")
        wf.write("\n")
        wf.write(f"with following keywords: {keywords}")
        wf.write("\n")
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