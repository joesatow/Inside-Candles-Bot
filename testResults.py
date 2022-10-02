falseSingleInsidesAAPL = [ 
    {
        'open': 147.64, 
        'high': 150.6414, 
        'low': 144.84, 
        'close': 149.84, 
        'volume': 146691387, 
        'datetime': 1664341200000
    }, 
    {
        'open': 146.1, 
        'high': 146.72, 
        'low': 140.68, 
        'close': 142.48, 
        'volume': 128138237, 
        'datetime': 1664427600000
    }, 
    {
        'open': 141.28, 
        'high': 143.1, 
        'low': 138.0, 
        'close': 138.2, 
        'volume': 124925274, 
        'datetime': 1664514000000
    }
]

trueSingleInsidesAAPL = [
    {
        "open": 147.64, 
        "high": 150.6414, 
        "low": 144.84, 
        "close": 149.84, 
        "volume": 146691387, 
        "datetime": 1664341200000
    },
    {
        "open": 147.64, 
        "high": 150.6414, 
        "low": 124.84, 
        "close": 149.84, 
        "volume": 146691387, 
        "datetime": 1664341200000
    },
    {
        "open": 147.64, 
        "high": 140.6414, 
        "low": 134.84, 
        "close": 149.84, 
        "volume": 146691387, 
        "datetime": 1664341200000
    }
]

falseDoubleInsidesAAPL = [
    {
        "open": 147.64, 
        "high": 150.6414, 
        "low": 144.84, 
        "close": 149.84, 
        "volume": 146691387, 
        "datetime": 1664341200000
    },
    {
        "open": 147.64, 
        "high": 150.6414, 
        "low": 144.84, 
        "close": 149.84, 
        "volume": 146691387, 
        "datetime": 1664341200000
    },
    {
        "open": 147.64, 
        "high": 150.6414, 
        "low": 144.84, 
        "close": 149.84, 
        "volume": 146691387, 
        "datetime": 1664341200000
    }
]

trueDoubleInsidesAAPL = [
    {
        "open": 147.64, 
        "high": 150.6414, 
        "low": 120.84, 
        "close": 149.84, 
        "volume": 146691387, 
        "datetime": 1664341200000
    },
    {
        "open": 147.64, 
        "high": 148.6414, 
        "low": 124.84, 
        "close": 149.84, 
        "volume": 146691387, 
        "datetime": 1664341200000
    },
    {
        "open": 147.64, 
        "high": 145.6414, 
        "low": 134.84, 
        "close": 149.84, 
        "volume": 146691387, 
        "datetime": 1664341200000
    }
]

falseSingleInsidesBABA = [
    {
        "open": 147.64, 
        "high": 150.6414, 
        "low": 144.84, 
        "close": 149.84, 
        "volume": 146691387, 
        "datetime": 1664341200000
    },
    {
        "open": 147.64, 
        "high": 150.6414, 
        "low": 144.84, 
        "close": 149.84, 
        "volume": 146691387, 
        "datetime": 1664341200000
    },
    {
        "open": 147.64, 
        "high": 150.6414, 
        "low": 144.84, 
        "close": 149.84, 
        "volume": 146691387, 
        "datetime": 1664341200000
    }
]

trueSingleInsidesBABA = [
    {
        "open": 147.64, 
        "high": 150.6414, 
        "low": 144.84, 
        "close": 149.84, 
        "volume": 146691387, 
        "datetime": 1664341200000
    },
    {
        "open": 147.64, 
        "high": 150.6414, 
        "low": 124.84, 
        "close": 149.84, 
        "volume": 146691387, 
        "datetime": 1664341200000
    },
    {
        "open": 147.64, 
        "high": 140.6414, 
        "low": 134.84, 
        "close": 149.84, 
        "volume": 146691387, 
        "datetime": 1664341200000
    }
]

falseDoubleInsidesBABA = [
    {
        "open": 147.64, 
        "high": 150.6414, 
        "low": 144.84, 
        "close": 149.84, 
        "volume": 146691387, 
        "datetime": 1664341200000
    },
    {
        "open": 147.64, 
        "high": 150.6414, 
        "low": 144.84, 
        "close": 149.84, 
        "volume": 146691387, 
        "datetime": 1664341200000
    },
    {
        "open": 147.64, 
        "high": 150.6414, 
        "low": 144.84, 
        "close": 149.84, 
        "volume": 146691387, 
        "datetime": 1664341200000
    }
]

trueDoubleInsidesBABA = [
    {
        "open": 147.64, 
        "high": 150.6414, 
        "low": 120.84, 
        "close": 149.84, 
        "volume": 146691387, 
        "datetime": 1664341200000
    },
    {
        "open": 147.64, 
        "high": 148.6414, 
        "low": 124.84, 
        "close": 149.84, 
        "volume": 146691387, 
        "datetime": 1664341200000
    },
    {
        "open": 147.64, 
        "high": 145.6414, 
        "low": 134.84, 
        "close": 149.84, 
        "volume": 146691387, 
        "datetime": 1664341200000
    }
]

testList = [
    falseSingleInsidesAAPL,
    trueSingleInsidesAAPL,
    falseDoubleInsidesAAPL,
    trueDoubleInsidesAAPL,
    falseSingleInsidesBABA,
    trueSingleInsidesBABA,
    falseDoubleInsidesBABA,
    trueDoubleInsidesBABA
]

def getTestList():
    return testList