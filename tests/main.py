import requests
import datetime
from datetime import datetime, timedelta
import math
key = "KM7SSWFJANTN4HOJIMYUGZAY1C09QWH3"

# number of days to subtract from current day to use with getting startDate
subtractedDays = 10

def timestamp(dt):
    epoch = datetime.utcfromtimestamp(0)
    return (dt - epoch).total_seconds() * 1000.0

currentYear = datetime.now().year
currentMonth = datetime.now().month
currentDay = datetime.now().day
todayMarketCloseTime = datetime(currentYear,currentMonth,currentDay,20,1,0)

endDate = math.trunc(timestamp(todayMarketCloseTime)) # datetime(year, month, day, hour, minute, second)
startDate = math.trunc(timestamp(todayMarketCloseTime-timedelta(days=subtractedDays))) # subtract specified days from endDate to get startDate

def call_TD_API():
    url = f"https://api.tdameritrade.com/v1/marketdata/AAPL/pricehistory?apikey={key}&periodType=day&frequencyType=minute&frequency=30&endDate={endDate}&startDate={startDate}&needExtendedHoursData=False"
    response = requests.request("GET", url, headers={}, data={})
    response = response.json()

    if list(response.keys())[0] == "error":
        #print("Reached max on: " + ticker[0] + ".  Trying again...")
        raise requests.exceptions.RequestException

    response = response['candles'] # only focus on candles part of API response
    return response

currentItem = call_TD_API()[-1]

time = int(currentItem['datetime'])/1000
dateConvertedTime = datetime.fromtimestamp(time).strftime('%H:%M')

with open('/Library/WebServer/Documents/Inside-Candles-Bot/tests/results.txt', 'a') as f:
    str = 'time: ' + datetime.now().strftime('%H:%M') + ", candle time: " + dateConvertedTime + ', low: ' + str(currentItem['low']) + ', high: ' + str(currentItem['high']) + ', open: ' + str(currentItem['open']) + ', close: ' + str(currentItem['close']) + ', volume: ' + str(currentItem['volume'])
    f.write(str)
    f.write('\n')