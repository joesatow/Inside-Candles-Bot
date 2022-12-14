import requests
import os
import time
from requests import Response
from urllib.parse import urlencode
from user_agent import generate_user_agent

user_agent = generate_user_agent()

def get_chart(ticker, period, size, chart_type,ta):
    """
        :param period: table period eg. : 'd', 'w' or 'm' for daily, weekly and monthly periods
        :param size: table size eg.: 'l' for large or 's' for small - choose large for better quality but higher size
        :param chart_type: chart type: 'c' for candles or 'l' for lines
        :param ta: technical analysis eg.: '1' to show ta '0' to hide ta
    """

    encoded_payload = urlencode(
            {"ty": chart_type, "ta": ta, "p": period, "s": size}
        )
    
    url = f"https://finviz.com/chart.ashx?{encoded_payload}&t={ticker}"
    response = finviz_request(url, user_agent)
    fileName = download_chart_image(response, url)
    return fileName

def finviz_request(url: str, user_agent: str) -> Response:
    response = requests.get(url, headers={"User-Agent": user_agent})
    return response

def download_chart_image(page_content: requests.Response, url,):
    """ Downloads a .png image of a chart into the "charts" folder. """
    file_name = f"{url.split('t=')[1]}_{int(time.time())}.png"

    with open(os.path.join("/Library/WebServer/Documents/charts/test-charts", file_name), "wb") as handle:
        handle.write(page_content.content)
    
    return file_name