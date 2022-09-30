import math
from datetime import datetime, timedelta

# number of days to subtract from current day to use with getting startDate
subtractedDays = 5

def timestamp(dt):
    epoch = datetime.utcfromtimestamp(0)
    return (dt - epoch).total_seconds() * 1000.0

currentYear = datetime.now().year
currentMonth = datetime.now().month
currentDay = datetime.now().day
todayMarketCloseTime = datetime(currentYear,currentMonth,currentDay,20,1,0)

endDate = math.trunc(timestamp(todayMarketCloseTime)) # datetime(year, month, day, hour, minute, second)
startDate = math.trunc(timestamp(todayMarketCloseTime-timedelta(days=subtractedDays))) # subtract specified days from endDate to get startDate

def getEndDate():
    return endDate

def getStatDate():
    return startDate
