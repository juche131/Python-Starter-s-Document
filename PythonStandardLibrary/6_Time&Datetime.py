import time
from datetime import datetime, timedelta

print(time.time())  # 1755515652.2721386
dt1 = datetime(2006, 4, 24)
print(dt1)  # 2006-04-24 00:00:00

print(datetime.now())  # 2025-08-18 19:14:41.571828

dt2 = datetime.strptime("2018/01/01", "%Y/%m/%d")
print(dt2)  # 2018-01-01 00:00:00
print(dt2.strftime("%y/%m"))  # 18/01

print(dt1 > dt2)  # False

dt2 = datetime.now()
duration = dt2-dt1
print(duration)  # 7056 days, 19:39:18.924955
print("days:", duration.days)
print("seconds:", duration.seconds)
print("seconds:", duration.total_seconds())  # seconds: 609709225.996912

dt3 = datetime(2018, 1, 1)+timedelta(days=1, seconds=114514)
print(dt3)  # 2018-01-03 07:48:34
