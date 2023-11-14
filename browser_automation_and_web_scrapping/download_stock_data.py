import requests
import time
from datetime import datetime

def convert_to_epoch(date_string):
    d = datetime.strptime(date_string, "%Y-%m-%d")
    epoch = time.mktime(d.timetuple())
    return int(epoch)

ticker = input("Enter ticker symbol:")
from_date = convert_to_epoch(input('Enter start date in YYYY-MM-DD format: '))
to_date = convert_to_epoch(input('Enter end date in YYYY-MM-DD format: '))


url = f"https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={from_date}&period2={to_date}&interval=1d&events=history&includeAdjustedClose=true"

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0. Safari/537.36"}
response = requests.get(url, headers=headers).content

#print(response)

with open('data.csv', 'wb') as f:
    f.write(response)


