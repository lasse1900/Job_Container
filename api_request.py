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

def start(offset, filename, keyword, location):
	print(f"def start-> offset: {offset}, filename: {filename}, keyword: {keyword}, location: {location}")
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
		try:
			response = requests.request("GET", url, headers=headers, params=querystring)
			time.sleep(6)
			response = json.loads(response.text)
			next_page = response[0]['next_page']

			if next_page == 'True':
				job_data.extend(response)
				offset += (10)
				start(offset, filename,keyword, location)
			else:
				job_data.extend(response)
				print("No more pages")
				json.dump(job_data, fp, indent=2, ensure_ascii=False, sort_keys=True)
				return
		except:
			print(response)
			print("Error happended while getting the response from API")
			print("next_page = response[0]['next_page']")
			print("KeyError: 0 - Please try soon again")
			sys.exit(1)

def main(offset, filename, keyword, location):
    start(offset, filename, keyword, location)
    
if __name__ == '__main__':	
	arg1_value = 0
	arg2_value = ""
	arg3_value = ""
	arg4_value = ""

    # Call the main function with the arguments
	main(arg1_value, arg2_value, arg3_value, arg4_value)