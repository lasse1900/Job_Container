import time
import pandas
from delete_oldfiles import delete_files
from api_request import main # running API-request
from append_json_files import parse_json_files_together
from sort_json import sort
from format_json import format_2_docx
from send_emails_with_attachments import send_email

# delete old files
delete_files()

# request open jobs with keywords given in search_terms.csv file
row_count = 0
keywords = []
file_params = pandas.read_csv('search_terms.csv')
for index, row in file_params.iterrows():
    sana = row['keyword']
    keywords.append(sana)
    keyword_index = index
    print(row['keyword'], row['location'])
    print("keyword: ", row['keyword'], " location: ", row['location'])
    main(f"input_{index}.json", row['keyword'], row['location'])
    row_count = index + 1

print(f"row count: {row_count}")
print(f"keywords: {keywords}")

time.sleep(5)
print("Hi, I'm appending files for 5 seconds..." )
# TODO for starters give the amount of params as an argument to parse_json_files_together()
parse_json_files_together(row_count)

time.sleep(5)
print("Hi, I'm sorting files for 5 seconds...")
# sort json file according to descending date
sort(row_count)

time.sleep(2)
print("Hi, I'm formating json to docx for 5 seconds...")
# formating json file into word document
format_2_docx()
time.sleep(2)
print("Hi, I'm sending email..." )
# sending jobs.docx according to the contacts.csv mailing list
send_email()

