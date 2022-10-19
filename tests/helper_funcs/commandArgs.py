import argparse
import sys

sys.tracebacklimit = 0

acceptableTimeframeInputs = ['1d','4h','1h']
acceptableSendTweetInputs = ['y','n','yes','no']

parser = argparse.ArgumentParser()
parser.add_argument("-tf", "--timeframe", help="Timeframe")
parser.add_argument("-st", "--sendtweet", help="Send Tweet")
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

def getArgs():
    return args