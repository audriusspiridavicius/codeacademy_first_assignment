while True:
    try:
        number = int(input("please enter a number: "))
        skaicius_ne_nulis = bool(number)
        if not number:
            break
    except ValueError:
       print("exeption vas raised")
    finally:
        print(skaicius_ne_nulis)
