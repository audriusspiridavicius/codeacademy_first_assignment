import datetime

training_days_list = []
exclude_dates = [datetime.datetime(2023, 5, 1), datetime.datetime(2023, 4, 24)]
date = datetime.datetime(2023, 4, 24)
end_date = datetime.datetime(2023, 10, 11)

day = datetime.timedelta(1)


while date <= end_date:

    is_working_day = date.strftime("%A").lower() != "sunday" and date.strftime("%A").lower() != "saturday"

    if date not in exclude_dates and is_working_day:
        training_days_list.append(date)
        print(date.strftime("%Y-%m-%d (%A)"))
    date += day
print(date)
print(end_date)
print(training_days_list)
