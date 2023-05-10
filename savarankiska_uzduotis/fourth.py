numbers = input("please enter number list separeted by space: ").split()

sum_of_numbers = sum([int(number) for number in numbers])
avrg = sum_of_numbers / len(numbers)

print(f"average of numbers is : {avrg}")
