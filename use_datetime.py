from datetime import datetime

now=datetime.now()
UTCnow=datetime.utcnow()
print(now)
print(UTCnow)
print(now.strftime('%a, %b %d %H:%M'))


dt=datetime(2015,10,15,20,20)
print(dt)
dtS=dt.timestamp()
print(dtS)
print(datetime.fromtimestamp(dtS))

cday=datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)