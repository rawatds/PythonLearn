from dateutil import tz, parser, relativedelta
from datetime import datetime

PYCON_DATE = parser.parse(("May 12, 2021 8:00AM"))
print(PYCON_DATE)

PYCON_DATE = PYCON_DATE.replace(tzinfo=tz.gettz("America/New_York"))
print("PYCON DATE : ", PYCON_DATE)

now_ist = datetime.now(tz=tz.tzlocal())
print("Current IST: ", now_ist)

delta_ist = relativedelta.relativedelta(PYCON_DATE, now_ist)
now_ny = datetime.now(tz=tz.gettz("America/New_York"))
print("Current NY: " , now_ny)



print(f"Time left with IST : {PYCON_DATE - now_ist} OR {delta_ist}")
print(f"Time left with NY  : {PYCON_DATE - now_ny}")

print("--------------- relativedelta ----------------------------")


now = datetime.now()
delta = relativedelta.relativedelta(years=5, days = +1, hours= -1, minutes=-20)
print(now)
print(now + delta)

delta = relativedelta.relativedelta(year=2010, month=1, day=15, hour=10, minute=20)
print(delta)
print(now + delta)

print("=========== formatted relativedelta ======================")
def time_amount(time_unit: str, countdown: relativedelta) -> str:
    t = getattr(countdown, time_unit)
    return f"{t} {time_unit}" if t != 0 else ""


countdown = relativedelta.relativedelta(PYCON_DATE, now_ist)
time_units = ["years", "months", "days", "hours", "minutes", "seconds"]
output = (t for tu in time_units if (t := time_amount(tu, countdown)))
print(output, type(output))

pycon_date_str = PYCON_DATE.strftime("%A, %B %d, %Y at %H:%M %p %Z")
print("Pycon date: ", pycon_date_str)
print("Countdown to PyCon US 2021:", ", ".join(output))

print( "Bye!")