import json
import datetime
from dateutil.relativedelta import relativedelta

today = datetime.date.today()
# Format the month with a single digit when needed
month_str = str(today.month) if today.month >= 10 else "" + str(today.month)
formatted_date = f"{today.day},{month_str},{today.year%1000}"
# Take todays date in same format as in API's JSON {"date": "11,05,23"}
DATE_TODAY = formatted_date
print(f"DATE_TODAY {DATE_TODAY}")

def filter():
    end_date = datetime.datetime.strptime(DATE_TODAY, '%d,%m,%y')
    end_date2 = end_date.strftime("%d,%m,%y")
    end_date_object = datetime.datetime.strptime(end_date2, "%d,%m,%y").date()

    start_date = end_date - relativedelta(months=1)
    start_date2 = start_date.strftime("%d,%m,%y")
    start_date_object = datetime.datetime.strptime(start_date2, "%d,%m,%y").date()    

    with open('sorted.json') as json_file:
        data = json.load(json_file)

    filtered_data = [obj for obj in data if start_date_object <= datetime.datetime.strptime(obj['date'], '%d-%m-%y').date() <= end_date_object]

    with open('filtered.json', 'w', encoding='utf-8') as fp:
        json.dump(filtered_data, fp, indent=2, ensure_ascii=False, sort_keys=True)
