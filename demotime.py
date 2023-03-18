from datetime import datetime, date
from pytz import timezone

fmt = "%Y-%m-%d %H:%M:%S %Z%z"
zone = 'US/Eastern'
ny_time = datetime.now(timezone(zone))
print('ny_time:{}, date:{}, time:{}'.format(ny_time.strftime(fmt),ny_time.date(),ny_time.time()))

timestamp = int(round(ny_time.timestamp()))
tt = ny_time.timestamp()
print("Integer timestamp of current datetime: ",timestamp, tt)
dateTimestamp = datetime.fromtimestamp(timestamp, tz=timezone(zone))
print('date from int timestamp: {}'.format(dateTimestamp))

end = datetime(2023,3,17,17,00,tzinfo=timezone(zone))
endTS  = int(round(end.timestamp()))
if ny_time<end:
    print(datetime(2023,3,17,17,00,tzinfo=timezone(zone)))
    print('endTimeStamp',endTS)
else:
    print('error')