#!/bin/bash

# remove previous requests response JSON files 
rm -f input_1.json
rm -f input_2.json

python request_jobs.py 0 input_1.json django tampere
sleep 2
python request_jobs.py 0 input_2.json "python developer" tampere

echo "Hi, I'm sleeping for 5 seconds..." 
sleep 5

python append_json_files.py

echo "Hi, I'm sleeping for 5 seconds..." 
sleep 5

python sort_json.py
sleep 1

python format.py

