import datetime

Get_date = input("please enter date (YYYY-MM-DD) ")#.split("-")
time_delta = datetime.timedelta(weeks=14)
try:
    #year, month, day = [int(item) for item in Get_date]
    #date = datetime.datetime(year, month, day)
    date = datetime.datetime.strptime(Get_date, "%Y-%m-%d")
except ValueError:
    print("opapa error")
    date = datetime.datetime.now()


d = date - time_delta

print(d.strftime("%Y - %B - %d - %A"))
