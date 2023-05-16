import json
from docx import Document
import pandas
import math
from datetime import datetime as dt
today = dt.today()
from ftfy import fix_encoding

# reading search terms from csv file
file_params = pandas.read_csv('search_terms.csv')
keywords = []
locations = []
for index, row in file_params.iterrows():
    sana = row['keyword']
    location = row['location']
    keywords.append(sana)
    locations.append(location)

def format_json_2_docx():
    # Open the JSON file for reading
    with open('filtered.json', 'r') as file:
        json_data = json.load(file)

    # Add the desired clause at the beginning
    modified_data = [{'data': json_data}]

    # Open the same JSON file for writing (which overwrites the existing file)
    with open('filtered_with_header.json', 'w') as file:
        json.dump(modified_data, file, indent=4)

    # sparate call to read line count
    with open("filtered.json", 'r', encoding="utf-8") as fp:
        for count, line in enumerate(fp):
            pass
    # print('Total Lines', count + 1)

    number_of_jobs = (count - 2)/17
    jobs = math.floor(number_of_jobs)
    # print(f'Number of jobs = [filtered.json lines/17]: {jobs}')

    subject = "Open Jobs at https://fi.indeed.com - " + today.strftime("%B %d, %Y")
    keyword_list = f"with following keywords: {keywords}"
    location_and_job_number = f"at{locations[0]} {jobs} open jobs"

    # Load JSON data from the file and add a JSON header
    with open('filtered_with_header.json', 'r') as json_file: 
        json_data = json.load(json_file)

    # Create a new Word document
    document = Document()

    # Iterate through JSON data and add content to the document
    for item in json_data:
        # Add the document title
        document.add_heading(subject, level=1)
        document.add_paragraph(keyword_list)
        document.add_paragraph(location_and_job_number)

        # Add sections to the document
        data = item['data']
        for section in data:
            company_name = section['company_name']
            job_title = section['job_title']
            date = section['date']
            job_location = section['job_location']
            job_url = section['job_url']

            # Add sections to docx
            document.add_heading(company_name, level=1)
            document.add_paragraph(job_title)        
            document.add_paragraph(job_url)
            document.add_paragraph(date)
            document.add_paragraph(job_location)
            document.add_paragraph('_'*25)

    document.save('jobs2.docx')
