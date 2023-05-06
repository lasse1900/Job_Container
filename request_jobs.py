import time
import os
import pandas
from api_request import main # running API-request
from append_json_files import parse_json_files_together
from sort_json import sort
from format_json import format_2_docx
from send_email_to_csv_contacts_once_a_day import send_email

# delete old files
# TODO make method of these deletetions
if os.path.exists("input_0.json"):
    os.remove("input_0.json")
if os.path.exists("input_1.json"):
    os.remove("input_1.json")
if os.path.exists("input_2.json"):
    os.remove("input_2.json")
if os.path.exists("input_3.json"):
    os.remove("input_3.json")
if os.path.exists("jobs.docx"):
    os.remove("jobs.docx")
if os.path.exists("sorted.json"):
    os.remove("sorted.json")
if os.path.exists("output.json"):
    os.remove("output.json")
if os.path.exists("output_temp.json"):
    os.remove("output_temp.json")    

# request open jobs with keywords given in search_terms.csv file
row_count = 0
keywords = []
file_params = pandas.read_csv('search_terms.csv')
for index, row in file_params.iterrows():
    sana = row['keyword']
    keywords.append(sana)
    keyword_index = index
    print(row['keyword'], row['location'])
    print(f" {row['keyword']} keyword with index: ",keyword_index)
    main(f"input_{index}.json", keywords[keyword_index])
    row_count = index + 1

print(f"row count: {row_count}")
print(f"keywords: {keywords}")

time.sleep(5)
print("Hi, I'm appending files for 5 seconds..." )
# TODO for starters give the amount of params as an argument to parse_json_files_together()
parse_json_files_together()

time.sleep(5)
print("Hi, I'm sorting files for 5 seconds...")
# sort json file according to descending date
sort()

time.sleep(2)
print("Hi, I'm formating json to docx for 5 seconds...")
# formating json file into word document
format_2_docx()
time.sleep(2)
print("Hi, I'm sending email..." )
# sending jobs.docx according to the contacts.csv mailing list
send_email()

