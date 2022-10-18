from helper_funcs.downloadFunctions import get_chart
from helper_funcs.twitterFunctions import sendTweet
from helper_funcs.mediaUpload import uploadMedia
from helper_funcs.dataFunctions import analyzeData
from testResults import getTestList

# Tracker variable to keep count of results found
countFound = 0

symbolsList = ['AAPL','AAPL','AAPL','AAPL','BABA','BABA','BABA','BABA']
priceDataList = getTestList()

# Analyze every stock, upload to twitter if anything found
for idx, symbol in enumerate(symbolsList):
    # Check for inside candles
    results = analyzeData(priceDataList[idx], symbol)

    # if any insides, get chart and upload to twit!
    if results['insidesFound'] == True:
        countFound += 1
        finvizChartFileName = get_chart(symbol, 'd','m','c',0)
        mediaID = uploadMedia(finvizChartFileName)
        sendTweet(results['tweetText'], mediaID)

print("Done. " + ("Nothing found." if countFound==0 else f"Found {countFound} cases."))