import datetime

date_now = datetime.datetime.now()

print(date_now)
print(date_now - datetime.timedelta(5))
print(date_now + datetime.timedelta(hours=8))
print(date_now.strftime("%Y %m %d, %I:%M:%S"))