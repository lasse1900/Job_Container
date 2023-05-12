import json
import datetime


def filter():
    today = datetime.date.today()
    formatted_date = today.strftime('%d-%m-%y')
    print(f"Date today is: {formatted_date} is short format (same as in json files)")

    # TODO these date should not be fixed, end date should be today and start date e.g. today - one month
    start_date = datetime.date(2023, 4, 1)
    end_date = datetime.date(2025, 12, 31)

    with open('sorted.json') as json_file:
        data = json.load(json_file)

    filtered_data = [obj for obj in data if start_date <= datetime.datetime.strptime(obj['date'], '%d-%m-%y').date() <= end_date]

    with open('filtered.json', 'w', encoding='utf-8') as fp:
        json.dump(filtered_data, fp, indent=2, ensure_ascii=False, sort_keys=True)

