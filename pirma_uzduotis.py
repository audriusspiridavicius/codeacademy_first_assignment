first_number = input("please enter first number ")
second_number = input("please enter second number ")

first_number = int(first_number)
second_number = int(second_number)

if first_number < second_number:
    print(f"a({first_number}) amzesnis uz b({second_number})")
    print(f"b / a = {second_number/first_number}")
elif first_number == second_number:
    print(f"a({first_number}) lygu b({second_number})")
    print(f"a({first_number}) + b({second_number}) = {first_number+second_number}")
else:
    print(f"a({first_number}) didesnis uz b({second_number})")
    print(f"a / b = {first_number/second_number}")