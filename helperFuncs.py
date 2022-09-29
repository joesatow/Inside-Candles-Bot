import math
import requests
import os
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

def get_chart(period, size, chart_type,ta):
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
    
    data_scrape(
        download_chart_image, 
        f"https://finviz.com/chart.ashx?{encoded_payload}&t={ticker}",
        user_agent
    )

def finviz_request(url: str, user_agent: str) -> Response:
    response = requests.get(url, headers={"User-Agent": user_agent})
    return response

def download_chart_image(page_content: requests.Response, **kwargs):
    """ Downloads a .png image of a chart into the "charts" folder. """
    file_name = f"{kwargs['URL'].split('t=')[1]}_{int(time.time())}.png"

    if not os.path.exists("charts"):
        os.mkdir("charts")

    with open(os.path.join("charts", file_name), "wb") as handle:
        handle.write(page_content.content)
    
def data_scrape(scrape_func, url, user_agent):
    response = finviz_request(url, user_agent)
    kwargs["URL"] = url
    data.append(scrape_func(response, *args, **kwargs))