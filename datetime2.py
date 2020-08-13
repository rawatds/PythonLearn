from datetime import time, date, datetime
import time as time2

print(time2.time())

cur_dt = date.today()
print(cur_dt)

now = datetime.now()
cur_tm = now.time()
cur_dt = now.date()

print(cur_dt, cur_tm)

print(now.isoformat(), cur_dt.isoformat(), cur_tm.isoformat(), sep=" / ")

print()

ds = '2020-01-01'
dt = date.fromisoformat(ds)
print(dt)

ts = '12:31:10'
tt = time.fromisoformat(ts)
print(ts)

nw = '2020-08-09T17:21:51'
nt = now.fromisoformat(nw)
print(nt)
print('--------------------')

7

