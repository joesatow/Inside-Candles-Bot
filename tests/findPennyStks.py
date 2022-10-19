from helper_funcs.TDA_Functions import call_TD_API
from helper_funcs.symbolsList import getSymbols
from tqdm import tqdm


# List of stock symbols to scan.  All optionable. Case sensitive.
symbolsList = getSymbols()

# Tracker variables to keep count of how many checked and results found
countChecked = 0
countFound = 0
newList = []
# Analyze every stock, upload to twitter if anything found
for symbol in tqdm(symbolsList, desc="Scanning symbols"):
    # Call TD API
    priceData = call_TD_API(symbol,"1d")

    try:
        if priceData[-1]['high'] > 15:
            newList.append(symbol)
    except:
        raise Exception(f"bad symbol: {symbol}")

print(newList)

print(f"Done. Checked {countChecked} stocks. " + ("Nothing found." if countFound==0 else f"Found {countFound} cases."))