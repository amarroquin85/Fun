import requests
import time
from datetime import datetime
ticker_symbol = input('Enter ticker symbol:')
from_date = input('Enter start date in this format yyyy/mm/dd:')
to_date = input('Enter end date in this format yyyy/mm/dd:')
dateF = datetime.strptime(from_date,'%Y/%m/%d')
dateT= datetime.strptime(to_date,'%Y/%m/%d')
from_epoch = int(time.mktime(dateF.timetuple()))
To_epoch = int(time.mktime(dateT.timetuple()))
url = f"https://query1.finance.yahoo.com/v7/finance/download/{ticker_symbol}?period1={from_epoch}&period2={To_epoch}&interval=1d&events=history&includeAdjustedClose=true"
headers = {"User-Agent":"Mozilla/5.0 (X11; Linux x86__64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}
content = requests.get(url, headers=headers).content
with open('data.csv','wb') as file:
    file.write(content)