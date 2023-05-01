import requests
import os
import json
from dotenv import load_dotenv
import time
import sys

load_dotenv()
token = os.environ.get("X-RapidAPI-Key")
url = "https://indeed-jobs-api-finland.p.rapidapi.com/indeed-fi/"
job_data = []

def start(offset, filename,keyword, location):
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
		
		# print(response.text)
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


def main(argv):
    offset = sys.argv[1]
    filename = sys.argv[2]
    print(f'filename: {filename}')
    keyword = sys.argv[3]
    print(f'keyword: {keyword}')
    print(f'{len(sys.argv)} argumets were given')
    
    if len(sys.argv) > 4:
       location = sys.argv[4]
       start(offset.__str__(), filename, keyword, location)
    else:
       start(offset.__str__(), filename, keyword, location='suomi')

if __name__ == '__main__':
    main(sys.argv[1:].__str__())