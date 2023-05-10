

def validate_text():

    while 1 > 0:
        user_text = input("please enter 5 words : ")
        user_text = user_text.split(" ")
        if len(user_text) == 5:
            break
        else:
            print("Invalid words count. Please enter correct number of words!!!")
    return user_text


text = validate_text()

for id, word in enumerate(text):
    print(f"{id+1}. {word}")

