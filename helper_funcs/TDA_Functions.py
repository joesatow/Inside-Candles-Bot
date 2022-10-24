from ratelimit import limits, sleep_and_retry
from backoff import on_exception, expo
import math
import requests
from datetime import datetime, timedelta
from helper_funcs.API_keys import getKey

# number of days to subtract from current day to use with getting startDate
subtractedDays = 10

# TD API key 
TD_API_Key = getKey('td_api_key')

def timestamp(dt):
    epoch = datetime.utcfromtimestamp(0)
    return (dt - epoch).total_seconds() * 1000.0

currentYear = datetime.now().year
currentMonth = datetime.now().month
currentDay = datetime.now().day
todayMarketCloseTime = datetime(currentYear,currentMonth,currentDay,20,1,0)

endDate = math.trunc(timestamp(todayMarketCloseTime)) # datetime(year, month, day, hour, minute, second)
startDate = math.trunc(timestamp(todayMarketCloseTime-timedelta(days=subtractedDays))) # subtract specified days from endDate to get startDate

# TDA API call for price data
@on_exception(expo, requests.exceptions.RequestException, max_time=60)
@sleep_and_retry
@limits(calls=120, period=60)
def call_TD_API(symbol, timeframe):
    if timeframe == '1d':
        url = f"https://api.tdameritrade.com/v1/marketdata/{symbol}/pricehistory?apikey={TD_API_Key}&periodType=month&frequencyType=daily&frequency=1&endDate={endDate}&startDate={startDate}"
    elif timeframe == '4h' or timeframe == '1h':
        url = f"https://api.tdameritrade.com/v1/marketdata/{symbol}/pricehistory?apikey={TD_API_Key}&periodType=day&frequencyType=minute&frequency=15&endDate={endDate}&startDate={startDate}&needExtendedHoursData=false"
    else:
        url = f"https://api.tdameritrade.com/v1/marketdata/{symbol}/pricehistory?apikey={TD_API_Key}&periodType=month&frequencyType=weekly&frequency=1&endDate={endDate}&startDate={math.trunc(timestamp(todayMarketCloseTime-timedelta(days=40)))}"

    response = requests.request("GET", url, headers={}, data={})
    response = response.json()

    if list(response.keys())[0] == "error":
        #print("Reached max on: " + ticker[0] + ".  Trying again...")
        raise requests.exceptions.RequestException

    response = response['candles'] # only focus on candles part of API response
    return response