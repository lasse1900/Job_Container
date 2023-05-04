import time
import os
from api_request import load_jobs
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

# get the amount of argument lines
with open(r"search_terms.txt", 'r') as fp:
    for count, line in enumerate(fp):
        pass
print('Total Lines', count + 1)

# request open jobs with keywords given in search_terms.txt file
# TODO count the number of parameters and act accordingly
with open("search_terms.txt") as file:
    lines = [line.rstrip() for line in file]
    print(lines[0])
    load_jobs("input_0.json", lines[0])
    print(lines[1])
    load_jobs("input_1.json", lines[1])
    print(lines[2])
    load_jobs("input_2.json", lines[2])
    print(lines[3])
    load_jobs("input_3.json", lines[3])

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

