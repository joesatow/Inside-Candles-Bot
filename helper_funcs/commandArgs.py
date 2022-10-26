import argparse
import sys
from helper_funcs.symbolsList import getSymbols, setSymbols
validSymbols = getSymbols()

sys.tracebacklimit = 0

acceptableTimeframeInputs = ['1d','4h','1h','1w']
acceptableSendTweetInputs = ['y','n','yes','no']

parser = argparse.ArgumentParser()
parser.add_argument("-tf", "--timeframe", help="Timeframe")
parser.add_argument("-st", "--sendtweet", help="Send Tweet")
parser.add_argument("-override", "--override", help="override symbols")
args = parser.parse_args()

if args.timeframe == None or args.sendtweet == None:
    raise Exception("Must use both flags -tf and -st. Exiting...")

if args.timeframe not in acceptableTimeframeInputs:
    raise Exception(f"Accetpabe time frame inputs are {*acceptableTimeframeInputs,}. Please try again...")

if args.sendtweet not in acceptableSendTweetInputs:
    raise Exception(f"Acceptable send tweet inputs are {*acceptableSendTweetInputs,}. Please try again...")

if args.sendtweet == 'y' or args.sendtweet == 'yes':
    args.sendtweet = True
else:
    args.sendtweet = False

if args.override:
    symbolInput = args.override.upper()
    if symbolInput in validSymbols:
        setSymbols(symbolInput)
    else:
        raise Exception("Invalid ticker...")

def getArgs():
    return args