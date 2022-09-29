import requests

# Get epoch time in MILLISECONDS for endDate = today, startDate = 2 days ago

url = "https://api.tdameritrade.com/v1/marketdata/AAPL/pricehistory?apikey=KM7SSWFJANTN4HOJIMYUGZAY1C09QWH3&periodType=month&period=1&frequencyType=daily&frequency=1"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)
response = response.json()

print(response['candles'][-1])
