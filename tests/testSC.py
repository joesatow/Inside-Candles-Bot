import requests
import os
import time
from helper_funcs.API_keys import getKey
from requests import Response
from urllib.parse import urlencode
from user_agent import generate_user_agent

sc_user = getKey("stock_charts_username")
sc_pass = getKey("stock_charts_pass")
user_agent = generate_user_agent()

# [0] = Daily, [1] = 4h
iValues = ['t9761318229c', 't0529553230c']
iValue = ''

def get_chart(symbol, tf):
    millisecondsEpoch = str(int(time.time()*1000))
    
    if tf == '1d':
        selector = 0
    if tf == '4h':
        selector = 1

    # [0] = Daily, [1] = 4h
    payloadObjects = [
        {"s": symbol, "p": "D", "b": "6", "g": '0', 'i': iValues[selector], 'r': millisecondsEpoch},
        {"s": symbol, "p:": "195", "b": "6", "g": "0", "i": iValues[selector], 'r': millisecondsEpoch}
    ]

    encoded_payload = urlencode(
            payloadObjects[selector]
        )
    
    url = f"https://stockcharts.com/c-sc/sc?{encoded_payload}"
    #url = "https://stockcharts.com/c-sc/sc?s=SRPT&p=195&b=6&g=0&i=t2018093905c&r=1666195519866"
    response = stockCharts_request(url, user_agent)
    fileName = download_chart_image(response, url)
    return fileName

def stockCharts_request(url: str, user_agent: str) -> Response:
    response = requests.get(url, headers={
        "cookie": f"_gcl_au=1.1.795530825.1659377303; _fssid=325716b4-c99c-47b5-a031-b65019fe1a0a; __qca=P0-1010041334-1659377306690; __gads=ID=2e19a88fdb6f684b:T=1659377307:S=ALNI_Mb1ir8zSaBTnz_QYjwH-odYg2vKPA; _cc_id=b1336d6ebfd1f2faaaf3e096772876a6; _pubcid=5cf22805-f814-4cdb-933c-712c81ffbef4; __gpi=UID=0000078dcec73a37:T=1659377307:RT=1660052105:S=ALNI_MYBgMSPS0Sz1qlDZ1ZmyMF6LFNvPA; cto_bundle=wZrSIV9jOTB0ckhXWTJwQ2Qyb21aZVkyWDVOM3BBbUZPbVhWM2lKb3I3RkdEUyUyRlZkUU1kZ25YNExhTSUyRm9NMFk0cCUyQmNlV1dKcVZZS0xYNWxEcGlvVG85S1BVckp3S0NHcVVDbDUyWXBDcmtsb2NGdU83TndPZ0RtcWZISUElMkZBTSUyRlJoTW5jRWRiSjVkR2ZwSXFCaHc3WTBuNDdnJTNEJTNE; cto_bidid=OXQe4F9WSHA1NCUyRktmbUhHRzE0JTJCNDlFNFhqa2Yxa2FIVGthOEx3T25ScXFYSlZPR0Y5c0RETTl0bkQzOWJteXBnTGZDJTJCYWdyNENSJTJCSTVrVmMlMkJLYnplUG9aaTBvcHBDQ204UEtDMnhVc2g0ZDh4UWZsd1EycEpIME9nTkx0eEhEZUp4dFU; SCCDashRows=hshhh; SCCDashMM=dow,2;sect;sp500-sctr,1;tc; JavaChartCode=1480617; SCCExtraID={sc_user}; SCCExtraPW={sc_pass}; _fbp=fb.1.1660067585884.940078008; sc2Pullouts=overStyles,indStyles; _gac_UA-88248853-1=1.1663858913.EAIaIQobChMIvsafpdWo-gIVwQ2tBh0mng_MEAAYASAAEgKBNfD_BwE; _gcl_aw=GCL.1663858913.EAIaIQobChMIvsafpdWo-gIVwQ2tBh0mng_MEAAYASAAEgKBNfD_BwE; _gid=GA1.2.1599941616.1666014809; mil=eyJpc0xvZ2dlZEluIjp0cnVlLCJ1c2VySWQiOiJqLnNhdG93QHlhaG9vLmNvbSIsImNoYXJ0Q29kZSI6IjE0ODA2MTciLCJmaXJzdE5hbWUiOiJKb3NlcGgiLCJsYXN0TmFtZSI6IlNhdG93IiwibWVtYmVyVHlwZSI6IkJBIiwibWVtYmVyUlQiOiIiLCJtZW1iZXJTdGF0dXMiOiJBIiwiaXNUZXJtc0FncmVlZCI6dHJ1ZSwic3RhcnREYXRlIjoiMjAxNy0wNy0yNiIsImV4cGlyYXRpb25EYXRlIjoiMjAyMi0xMS0wNyIsIm5hbWUiOiJKb3NlcGgifQ==; _gat_gtag_UA_88248853_1=1; _ga=GA1.2.2057403740.1659377303; SCCLogin2=LlOOOMMNmlpdlNPLOlodqQ.1480617.C.; ChartXmlId={iValue}; _ga_MPHC369VQR=GS1.1.1666193845.201.1.1666195520.0.0.0",
        "User-Agent": user_agent
        })
    return response

def download_chart_image(page_content: requests.Response, url,):
    """ Downloads a .png image of a chart into the "charts" folder. """
    file_name = f"{url.split('s=')[1].split('&')[0]}_{int(time.time())}.png"

    with open(os.path.join("/Library/WebServer/Documents/charts/test-charts", file_name), "wb") as handle:
        handle.write(page_content.content)
    
    return file_name

get_chart('aapl', '1d')