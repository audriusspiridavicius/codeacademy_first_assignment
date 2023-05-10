import datetime

old = []
new = []

for i in range(0, 1000000):
    old.append(i * 2)

start_time = datetime.datetime.now()

for number in old:
    new.append(number * 2)

finish_time = datetime.datetime.now()
result_time = finish_time - start_time

print(result_time)

new2 = []
start_time = datetime.datetime.now()

new2 = [number * 2 for number in old]

finish_time = datetime.datetime.now()
result_time = finish_time - start_time

print(type(result_time))
print(result_time)
