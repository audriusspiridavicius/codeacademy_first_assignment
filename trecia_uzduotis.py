text = "Sometimes weak and wan, sometimes strong and full of light. The moon understands what it means to be human."
#text = "Runaway heirs have their reasons for getting out. But, in the lost heir trope, there is an understanding that they will have to come back. A kingdom is about to crumble under the rule of a cruel tyrant"
sentences = text.split(". ")

print(sentences[0])
print(sentences[1])
text2 = f"{sentences[0]}. {sentences[1]}"
print(f"{sentences[0].lower()}. {sentences[1].lower()}")
print(text2)
print(text2[::-1])
