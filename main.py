from helper_funcs.downloadFunctions import get_chart
from helper_funcs.twitterFunctions import sendTweet
from helper_funcs.mediaUpload import uploadMedia
from helper_funcs.TDA_Functions import call_TD_API
from helper_funcs.symbolsList import getSymbols
from helper_funcs.dataFunctions import analyzeData
from tqdm import tqdm

# List of stock symbols to scan.  All optionable. Case sensitive.
symbolsList = getSymbols()

# Tracker variable to keep count of results found
countFound = 0

# Analyze every stock, upload to twitter if anything found
for symbol in tqdm(symbolsList, desc="Scanning symbols"):
    # Call TD API
    priceData = call_TD_API(symbol)

    # Check for inside candles
    results = analyzeData(priceData, symbol) 

    # if any insides, get chart and upload to twit!
    if results['insidesFound']:
        countFound += 1
        finvizChartFileName = get_chart(symbol, 'd','m','c',0)
        mediaID = uploadMedia(finvizChartFileName)
        sendTweet(results['tweetText'], mediaID)

print("Done. " + ("Nothing found." if countFound==0 else f"Found {countFound} cases."))   