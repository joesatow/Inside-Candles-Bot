from helper_funcs.TDA_Functions import call_TD_API
from helper_funcs.downloadFunctions import get_chart
from helper_funcs.twitterFunctions import sendTweet
from helper_funcs.mediaUpload import uploadMedia
# List of stock symbols to scan.  All optionable. Case sensitive.
symbolsList = ['AAPL']

for symbol in symbolsList:
    # Call TD API
    # priceData = call_TD_API(symbol)

    # # Parse priceData into variables
    # today, yesterday, twoDaysAgo = priceData[-1], priceData[-2], priceData[-3]

    # # Check for single inside day
    # insideHighs = today['high'] < yesterday['high']
    # insideLows = today['low'] > yesterday['low']

    # if insideHighs and insideLows:
    #     # get chart
    #     # send tweet
    #     pass

    # # Check for double inside days
    # doubleInsideHighs = insideHighs and yesterday['high'] < twoDaysAgo['high']
    # doubleInsideLows = insideLows and yesterday['low'] > twoDaysAgo['low']

    finvizChartFileName = get_chart('AAPL', 'd','l','c',0)
    mediaKeys = uploadMedia(finvizChartFileName)
    #sendTweet(finvizChartResponse.content)
