import datetime
import math

acceptableHours = ['09:30','9:45','10:00','10:15','10:30','10:45','11:00','11:15','11:30','11:45','12:00','12:15','12:30','12:45','13:00','13:15','13:30','13:45','14:00','14:15','14:30','14:45','15:00','15:15','15:30','15:45']

def getCandles(data, tf):
    index = -1
    currentHigh = 0
    currentLow = math.inf
    candles = []

    if tf == '1d':
        return data

    if tf == '1w':
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
                #print(dateConvertedTime, currentLow, currentHigh)
                candles.insert(0,{"low": currentLow,"high": currentHigh})
                currentHigh = 0
                currentLow = math.inf
                
        if tf == '4h':
            if dateConvertedTime == '12:45' or dateConvertedTime == '09:30':
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

    if timeframe == '1d':
        text = 'daily'
    elif timeframe == '1w':
        text = 'weekly'
    elif timeframe == '4h':
        text = '4h'
    elif timeframe == '1h':
        text = 'hourly'

    if tripleInsideHighs and tripleInsideLows:
        insidesFound = True
        tweetText = f"TRIPLE inside {text} candles found for ${symbol}"
    elif doubleInsideHighs and doubleInsideLows: 
        insidesFound = True
        tweetText = f"Double inside {text} candles found for ${symbol}"
    # elif insideHighs and insideLows: 
    #     insidesFound = True
    #     tweetText = f"Single inside candle found for ${symbol}"

    resultsObject = {
        "insidesFound": insidesFound,
        "tweetText": tweetText
    }

    return resultsObject
