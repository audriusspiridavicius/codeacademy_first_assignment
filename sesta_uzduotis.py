first_number = float(input("Iveskite pirma skaiciu: "))
second_number = float(input("Iveskite antra skaiciu: "))
third_number = float(input("Iveskite trecia skaiciu: "))

min_number = 0
max_number = 0

if first_number > second_number:
    max_number = first_number
    min_number = second_number
else:
    max_number = second_number
    min_number = first_number

if third_number > max_number:
    max_number = third_number
elif third_number < min_number:
    min_number = third_number

print(f"max number is : {max_number}")
print(f"max number is : {min_number}")
