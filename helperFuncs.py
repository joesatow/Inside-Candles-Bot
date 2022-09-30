import math
import requests
import os
import time
from requests import Response
from datetime import datetime, timedelta
from urllib.parse import urlencode
from user_agent import generate_user_agent

user_agent = generate_user_agent()
def timestamp(dt):
    epoch = datetime.utcfromtimestamp(0)
    return (dt - epoch).total_seconds() * 1000.0

currentYear = datetime.now().year
currentMonth = datetime.now().month
currentDay = datetime.now().day
todayMarketCloseTime = datetime(currentYear,currentMonth,currentDay,20,1,0)
endDate = math.trunc(timestamp(todayMarketCloseTime)) # datetime(year, month, day, hour, minute, second)
startDate = math.trunc(timestamp(todayMarketCloseTime-timedelta(days=2))) # subtract two days

def getEndDate():
    return endDate

def getStatDate():
    return startDate

def get_chart(ticker, period, size, chart_type,ta):
    """
        :param period: table period eg. : 'd', 'w' or 'm' for daily, weekly and monthly periods
        :type period: str
        :param size: table size eg.: 'l' for large or 's' for small - choose large for better quality but higher size
        :type size: str
        :param chart_type: chart type: 'c' for candles or 'l' for lines
        :type chart_type: str
        :param ta: technical analysis eg.: '1' to show ta '0' to hide ta
        :type ta: str
    """

    encoded_payload = urlencode(
            {"ty": chart_type, "ta": ta, "p": period, "s": size}
        )
    
    url = f"https://finviz.com/chart.ashx?{encoded_payload}&t={ticker}"
    response = finviz_request(url, user_agent)
    download_chart_image(response, url)

def finviz_request(url: str, user_agent: str) -> Response:
    response = requests.get(url, headers={"User-Agent": user_agent})
    print(response)
    return response

def download_chart_image(page_content: requests.Response, url,):
    """ Downloads a .png image of a chart into the "charts" folder. """
    file_name = f"{url.split('t=')[1]}_{int(time.time())}.png"

    if not os.path.exists("charts"):
        os.mkdir("charts")

    with open(os.path.join("charts", file_name), "wb") as handle:
        handle.write(page_content.content)
    

