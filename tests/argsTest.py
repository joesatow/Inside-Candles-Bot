import argparse

parser = argparse.ArgumentParser()

# -tf TIMEFRAME
parser.add_argument("-tf", "--timeframe", help="Timeframe")

args = parser.parse_args()

print(args.timeframe)