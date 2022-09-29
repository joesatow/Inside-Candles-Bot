import requests
from helperFuncs import getEndDate, getStatDate, get_chart

# Grab dates from helper function
endDate = getEndDate()
startDate = getStatDate()

# API call
url = f"https://api.tdameritrade.com/v1/marketdata/AAPL/pricehistory?apikey=KM7SSWFJANTN4HOJIMYUGZAY1C09QWH3&periodType=month&frequencyType=daily&frequency=1&endDate={endDate}&startDate={startDate}"
response = requests.request("GET", url, headers={}, data={})
response = response.json()['candles'] # only focus on candles part of API response

# Parse response into variables
today, yesterday, twoDaysAgo = response[-1], response[-2], response[-3]

# Check for single inside day
insideHighs = today['high'] < yesterday['high']
insideLows = today['low'] > yesterday['low']

if insideHighs and insideLows:
    print

# Check for double inside days
doubleInsideHighs = insideHighs and yesterday['high'] < twoDaysAgo['high']
doubleInsideLows = insideLows and yesterday['low'] > twoDaysAgo['low']

