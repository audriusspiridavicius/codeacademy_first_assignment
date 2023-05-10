import random

number = random.randint(1, 100)
max_guess_count = 7

#print(number)
correct_gues = False
too_big_guess_message = "Per didelis, bandykite vel"
too_small_guess_message = "Per mazas, bandykite vel"
guess_count = 0
while not correct_gues and guess_count != max_guess_count:
    user_input = int(input("spekite skaiciu: "))
    if user_input > number:
        print(too_big_guess_message)
    elif user_input < number:
        print(too_small_guess_message)
    else:
        correct_gues = True
        print(f"Sveikiname atspejote. Paslaptingasis skaicius yra {number}")
    guess_count += 1
if guess_count == max_guess_count and correct_gues is False:
    print("isnaudojote spejimu limita. Zaidimas pralaimetas")