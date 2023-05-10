sum = 0
while True:
    number = float(input("Please enter any number: "))
    if number < 0:
        break
    else:
        sum += number
print(sum)

