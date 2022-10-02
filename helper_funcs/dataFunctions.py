def analyzeData(priceData, symbol):
    insidesFound = False
    tweetText = ""

     # Parse priceData into variables
    today, yesterday, twoDaysAgo = priceData[-1], priceData[-2], priceData[-3]

    # Check for single inside day
    insideHighs = today['high'] < yesterday['high']
    insideLows = today['low'] > yesterday['low']

    # Check for double inside days
    doubleInsideHighs = insideHighs and yesterday['high'] < twoDaysAgo['high']
    doubleInsideLows = insideLows and yesterday['low'] > twoDaysAgo['low']

    if doubleInsideHighs and doubleInsideLows: # Check double inside days
        insidesFound = True
        tweetText = f"Double inside candles found for ${symbol}"
    elif insideHighs and insideLows: # If above not true, check for single inside days
        insidesFound = True
        tweetText = f"Single inside candles found for ${symbol}"

    resultsObject = {
        "insidesFound": insidesFound,
        "tweetText": tweetText
    }

    return resultsObject
