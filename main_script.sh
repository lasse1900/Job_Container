#!/bin/bash

# remove previous requests response JSON files 
rm -f input_1.json
rm -f input_2.json
rm -f formated.md
rm -f output.json
rm -f sorted.json
rm -f jobs.docx

sleep 5
#      argv 1          argv 2       argv 3
python request_jobs.py input_1.json embedded
sleep 2
#      argv 1          argv 2       argv 3             argv 4
python request_jobs.py input_2.json "python developer" tampere

echo "Hi, I'm appending files for 5 seconds..." 
sleep 5

python append_json_files.py

echo "Hi, I'm sorting files for 5 seconds..." 
sleep 5

python sort_json.py
sleep 1

echo "Hi, I'm formating json to docx for 5 seconds..." 
python format.py

echo "Hi, I'm sending email..." 
python send_email_to_csv_contacts_once_a_day.py