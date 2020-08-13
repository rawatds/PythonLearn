import datetime, pytz

d1 = datetime.date(2020, 8, 3)
print(d1)

tday = datetime.date.today()
print(tday)
print(tday.year, tday.month, tday.day)

print(tday.weekday(), tday.isoweekday())

tdelta = datetime.timedelta(days=7)

print(tday + tdelta)
print(tday - tdelta)

bday = datetime.date(2020, 11, 18)

till_days = bday - tday

print(till_days)
print(till_days.days, till_days.seconds, till_days.total_seconds())
print( till_days.seconds)
print("------------------------------")

t1 = datetime.time(13, 6, 45)
print(t1)
print(t1.hour, t1.minute, t1.second, t1.microsecond)

print()

curtime = datetime.datetime.now()

print(datetime.datetime.now().date())
print(datetime.datetime.now().time())
print("Now: ", datetime.datetime.now())
print("Today: ", datetime.datetime.today())
print()

dt1 = datetime.datetime(2020, 8, 7, 12, 30, 45, 100000)
print(dt1)
print(dt1.date())
print(dt1.time())
print(dt1.now())

print()
tdelta = datetime.timedelta(days=7)
print(dt1  + tdelta)
print(dt1  - tdelta)

print()
tdelta = datetime.timedelta(hours=12)
print(dt1 + tdelta)
print(dt1 - tdelta)

print("-----------------")

dt_today =  datetime.datetime.today()
dt_now =  datetime.datetime.now()
dt_utcnow =  datetime.datetime.utcnow() 

print("Today  : ", dt_today)
print("Now    : ", dt_now)
print("UTCNow : ", dt_utcnow)

print("'''''''''''' timezone aware ==============")
dt = datetime.datetime(2020, 8, 7 , 15, 30, 45)
dz = datetime.datetime(2020, 8, 7 , 15, 30, 45, tzinfo=pytz.timezone( "Asia/Calcutta"))
print("dt : ", dt )
print("dz : ", dz )


print('-----------------')
utcnow = datetime.datetime.now(tz=pytz.UTC)
istnow = datetime.datetime.now(tz=pytz.timezone("Asia/Calcutta"))
utcnow2 = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print("UTC Now : ", utcnow)
print("IST Now : ", istnow)
print("UTC2 Now: ", utcnow2)


dt_london1 = istnow.astimezone(pytz.timezone( "Europe/London"))
print("London1: ", dt_london1)

dt_london2 = utcnow.astimezone(pytz.timezone( 'America/Los_Angeles'))
print("London2: ", dt_london2)

print('-------------------------------------')

dt_local =  datetime.datetime.now()
dt_now = datetime.datetime.now(tz=pytz.timezone("Asia/Calcutta"))
dt_london = datetime.datetime.now(tz=pytz.timezone("Europe/London"))
print(dt_local.isoformat())
print(dt_now.isoformat())
print(dt_london.isoformat())

print(dt_now.strftime('%B %d, %Y'))


s = 'November 18, 2020'
dt = datetime.datetime.strptime(s, '%B %d, %Y')
print(dt)