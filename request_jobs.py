import time
import pandas
import csv
from delete_oldfiles import delete_files
from api_request import main # running API-request
from append_json_files import parse_json_files_together
from sort_json import sort
from format_json import format_2_docx
from format_json_to_docx import format_json_2_docx
from send_emails_with_attachments import send_email
from filter_json import filter
import math

# delete old files
delete_files()

# request open jobs with keywords given in search_terms.csv file
row_count = 0
filenames = []
keywords = []
locations = []
offset = 0
location = ''
boolean_2_stripped = True

file_params = pandas.read_csv('search_terms.csv')
for index, row in file_params.iterrows():
    keyword = row['keyword']
    keyword_stripped = keyword.strip()
    keywords.append(keyword_stripped)
    print(f"index 1: {index}")
    location = row['location']
    try: 
        if math.isnan(location):
            print(f"index 2 : {index}")
            location = 'Suomi'
            print(f"location set to default: {location} and {keyword}")
            locations.append(location) 
    except:
        boolean_2_stripped = True
        location_stripped = location.strip()
        print(f"index 3: {index}")
        print(f"location given as csv-file input: {location} and {keyword}")
        locations.append(location_stripped) 

    print(f"offset: {offset}, input_{index}.json, {keywords[index]}, {locations[index]}")
    main(offset, f"input_{index}.json", f"{keywords[index]}", f"{locations[index]}")
    row_count = index + 1
    print(locations)

# In case locations are missing and default location 'Suomi' is added into list
csv_file = "temp.csv"
# Open the CSV file in write mode
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(locations)

time.sleep(5)
print("Hi, I'm appending files for 5 seconds..." )
print(f"row_amount in request_jobs: {row_count} ")
# Give the amount of params as an argument to parse_json_files_together()
parse_json_files_together(row_count)

time.sleep(5)
print("Hi, I'm sorting files for 5 seconds...")
# sort json file according to descending date, file indexing starting from 0
sort()

time.sleep(5)
print("Hi, I'm filtering file for 5 seconds...")
# filter json file dropping out old jobs
filter()

time.sleep(2)
print("Hi, I'm formating (with Pypandox-library) json to docx for 5 seconds...")
# formating json file into word document
format_2_docx()

time.sleep(2)
print("Hi, I'm formating (with docx library) json to docx for 5 seconds...")
# formating json file into word document
format_json_2_docx()

# sending jobs.docx according to the contacts.csv mailing list
try:
    print("Hi, I'm sending email..." )
    send_email()
except:
    print("Error with email sending, email-server might be down for some reason!")