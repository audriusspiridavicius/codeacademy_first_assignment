first_number = float(input("Iveskite pirma skaiciu: "))
second_number = float(input("Iveskite antra skaiciu: "))

operation = input("koki veiksma norite atliktis(+ - * /)?")[0]
result = 0
if operation == "+":
    result = first_number + second_number
elif operation == "-":
    result = first_number - second_number
elif operation == "*":
    result = first_number * second_number
elif operation == "/":
    result = first_number / second_number
else:
    result = "ivedete klaidinga veiksma"


print(f"rezultatas = {result}")