
words = input("please enter your sentence: ").split(" ")
words.sort()
for word in words:
    print(word)
print("\n")
print("printing lists in new line")
print(words, sep="\n")
print(*words, sep="\n")