import time
import pandas
from delete_oldfiles import delete_files
from api_request import main # running API-request
from append_json_files import parse_json_files_together
from sort_json import sort
from format_json import format_2_docx
from send_emails_with_attachments import send_email
from filter_json import filter

# delete old files
delete_files()

# request open jobs with keywords given in search_terms.csv file
row_count = 0
filenames = []
keywords = []
locations = []
offset = 0

file_params = pandas.read_csv('search_terms.csv')
for index, row in file_params.iterrows():
    keyword = row['keyword']
    keyword_stripped = keyword.strip()
    keywords.append(keyword_stripped)
    location = row['location']
    location_stripped = location.strip()
    locations.append(location_stripped)   

    print(f"offset: {offset}, input_{index}.json, {keywords[index]}, {locations[index]}")
    main(offset, f"input_{index}.json", f"{keywords[index]}", f"{locations[index]}")
    row_count = index + 1

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
print("Hi, I'm formating json to docx for 5 seconds...")
# formating json file into word document
format_2_docx()
time.sleep(2)
print("Hi, I'm sending email..." )
# sending jobs.docx according to the contacts.csv mailing list
send_email()
