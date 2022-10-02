def analyzeData(priceData):
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

    resultsObject = {
        "insidesFound": insidesFound,
        "tweetText": tweetText
    }

    return resultsObject
