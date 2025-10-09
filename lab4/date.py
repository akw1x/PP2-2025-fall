from datetime import date, datetime, timedelta

#1
def five_day():
    today = date.today()
    a = today - timedelta(days=5)

    print(today)
    print(a)

five_day()
print()

#2
def yest_tod_tom():
    today = date.today()
    yest = today - timedelta(days=1)
    tom = today + timedelta(days=1)

    print (yest)
    print(today)
    print(tom)

yest_tod_tom()
print()

#3
def mic(dt: datetime | None = None):
    dt = dt or datetime.now()
    x = dt.replace(microsecond=0)
    y = dt.isoformat(timespec="seconds")

    print(dt)
    print(x)
    print(y)

mic()
print()

#4
def diff(a: datetime, b: datetime):
    delta = b - a
    return int(delta.total_seconds())

t1 = datetime(2025, 10, 1, 12, 0, 0)
t2 = datetime(2025, 10, 9, 15, 30, 45)
print(diff(t1, t2))