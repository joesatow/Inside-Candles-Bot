import datetime
import math

acceptableHours = ['09:30','10:00','10:30','11:00','11:30','12:00','12:30','13:00','13:30','14:00','14:30','15:00','15:30']

def getCandles(data, tf):
    index = -1
    currentHigh = 0
    currentLow = math.inf
    candles = []

    if tf == '1d':
        return data

    while len(candles) < 4:
        currentItem = data[index]
        time = int(currentItem['datetime'])/1000
        dateConvertedTime = datetime.datetime.fromtimestamp(time).strftime('%H:%M')
        if dateConvertedTime not in acceptableHours:
            index -= 1
            continue 
        
        currentHigh = max(currentHigh, currentItem['high'])
        currentLow = min(currentLow, currentItem['low'])
        
        if tf == '1h': 
            if dateConvertedTime.split(":")[1] == '00':
                candles.insert(0,{"low": currentLow,"high": currentHigh})
                currentHigh = 0
                currentLow = math.inf
                
        if tf == '4h':
            if dateConvertedTime == '13:00' or dateConvertedTime == '09:30':
                candles.insert(0,{"low": currentLow,"high": currentHigh})
                currentHigh = 0
                currentLow = math.inf
            
        index -= 1
    
    return candles

def analyzeData(priceData, symbol, timeframe):
    insidesFound = False
    tweetText = ""

    # Get candles list
    candles = getCandles(priceData, timeframe)

    # Parse priceData into variables
    mostRecentCandle, secondMostRecentCandle, thirdMostRecentCandle, fourthMostRecentCandle = candles[-1], candles[-2], candles[-3], candles[-4]

    # Check for single inside day
    insideHighs = mostRecentCandle['high'] < secondMostRecentCandle['high']
    insideLows = mostRecentCandle['low'] > secondMostRecentCandle['low']

    # Check for double inside days
    doubleInsideHighs = insideHighs and secondMostRecentCandle['high'] < thirdMostRecentCandle['high']
    doubleInsideLows = insideLows and secondMostRecentCandle['low'] > thirdMostRecentCandle['low']

    # Check for triple inside days
    tripleInsideHighs = doubleInsideHighs and thirdMostRecentCandle['high'] < fourthMostRecentCandle['high']
    tripleInsideLows = doubleInsideLows and thirdMostRecentCandle['low'] > fourthMostRecentCandle['low']

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
