from helper_funcs.downloadFunctions import get_chart
from helper_funcs.twitterFunctions import sendTweet
from helper_funcs.mediaUpload import uploadMedia
from helper_funcs.TDA_Functions import call_TD_API
from helper_funcs.symbolsList import getSymbols
from helper_funcs.dataFunctions import analyzeData
from helper_funcs.commandArgs import getArgs
from tqdm import tqdm

# Get command line args
args = getArgs()
timeframeFlag, sendTweetFlag = args.timeframe, args.sendtweet

# List of stock symbols to scan.  All optionable. Case sensitive.
symbolsList = getSymbols()

# Tracker variables to keep count of how many checked and results found
countChecked = 0
countFound = 0

# Analyze every stock, upload to twitter if anything found
for symbol in tqdm(symbolsList, desc="Scanning symbols"):
    # Call TD API
    #### Based on timeframeFlag, adjust endTime in API call to last time you want.
    priceData = call_TD_API(symbol, timeframeFlag)

    # Check for inside candles
    results = analyzeData(priceData, symbol, timeframeFlag) 

    # if any insides, get chart and upload to twit!
    if results['insidesFound']:
        countFound += 1
        finvizChartFileName = get_chart(symbol, timeframeFlag)
        if countFound < 4:
            if sendTweetFlag:
                mediaID = uploadMedia(finvizChartFileName)
                sendTweet(results['tweetText'], mediaID)
    
    countChecked += 1

print(f"Done. Checked {countChecked} stocks. " + ("Nothing found." if countFound==0 else f"Found {countFound} cases."))