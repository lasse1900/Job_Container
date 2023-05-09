import requests
import os
import json
from dotenv import load_dotenv
import time
import sys
import inspect

load_dotenv()
token = os.environ.get("X-RapidAPI-Key")
url = "https://indeed-jobs-api-finland.p.rapidapi.com/indeed-fi/"
job_data = []

def start(offset, filename, keyword, location):
	num_args0 = len(inspect.signature(start).parameters)
	print(f"location: -------> {location}")
	print("def start(...) number of args", num_args0)
	print(f"at start-> filename: {filename}, keyword: {keyword}, location: {location}")
	with open(filename, 'a+', encoding='utf-8') as fp:
		querystring = {
			"offset": f"{offset}", 
			"keyword": keyword, 
			"location": location
		}
		headers = {
			"content-type": "application/json",
			"X-RapidAPI-Key": token,
			"X-RapidAPI-Host": "indeed-jobs-api-finland.p.rapidapi.com"
		}

		response = requests.request("GET", url, headers=headers, params=querystring)
		time.sleep(6)
		response = json.loads(response.text)
		next_page = response[0]['next_page']

		if next_page == 'True':
			job_data.extend(response)
			offset += str(10)
			start(offset, filename,keyword, location)
		else:
			job_data.extend(response)
			print("No more pages")
			json.dump(job_data, fp, indent=2, ensure_ascii=False, sort_keys=True)
			return

def main(filename, keyword, location):
    offset = "0" # RapidAPI specific to read 10 jobs on one searchpage
    print("argumentit ---> ", filename, " -- ", keyword, " -- ", location)
    num_args = len(inspect.signature(main).parameters)
    
    if num_args == 3:
       print(f"location: {location} ")
       start(offset.__str__(), filename, keyword, location)
    else:
       start(offset.__str__(), filename, keyword, location='suomi')

if __name__ == '__main__':
    main(sys.argv[0:].__str__())