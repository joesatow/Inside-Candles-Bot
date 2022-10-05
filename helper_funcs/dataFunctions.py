def analyzeData(priceData, symbol):
    insidesFound = False
    tweetText = ""

     # Parse priceData into variables
    try:
        today, yesterday, twoDaysAgo, threeDaysAgo = priceData[-1], priceData[-2], priceData[-3], priceData[-4]
    except:
        print("price data should be below here")
        print("problematic symbol: " + symbol)
        print(priceData)
        print("price data should be above here")
        raise Exception("error found")

    # Check for single inside day
    insideHighs = today['high'] < yesterday['high']
    insideLows = today['low'] > yesterday['low']

    # Check for double inside days
    doubleInsideHighs = insideHighs and yesterday['high'] < twoDaysAgo['high']
    doubleInsideLows = insideLows and yesterday['low'] > twoDaysAgo['low']

    # Check for triple inside days
    tripleInsideHighs = doubleInsideHighs and twoDaysAgo['high'] < threeDaysAgo['high']
    tripleInsideLows = doubleInsideLows and twoDaysAgo['low'] > threeDaysAgo['low']

    if tripleInsideHighs and tripleInsideLows:
        insidesFound = True
        tweetText = f"TRIPLE inside candles found for ${symbol}"
    elif doubleInsideHighs and doubleInsideLows: 
        insidesFound = True
        tweetText = f"Double inside candles found for ${symbol}"
    # elif insideHighs and insideLows: 
    #     insidesFound = True
    #     tweetText = f"Single inside candle found for ${symbol}"

    resultsObject = {
        "insidesFound": insidesFound,
        "tweetText": tweetText
    }

    return resultsObject
