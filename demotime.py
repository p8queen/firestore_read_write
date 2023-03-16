from datetime import datetime
from pytz import timezone

fmt = "%Y-%m-%d %H:%M:%S %Z%z"
timezonelist = ['UTC','US/Pacific','Europe/Berlin']
for zone in timezonelist:
    now_time = datetime.now(timezone(zone))
    print(now_time.strftime(fmt))


print('local time')
local_dt = datetime.now()
print("Current datetime: ", local_dt)
timestamp = int(round(local_dt.timestamp()))
tt = local_dt.timestamp()
print("Integer timestamp of current datetime: ",timestamp, tt)
date = datetime.fromtimestamp(timestamp )
print('date from int timestamp: {}'.format(date))
