import random

skaiciai = []
print(type(skaiciai))
for i in range(3):
    skaiciai.append(random.randint(1, 6))
if len([number for number in skaiciai if number==5]):
    print("pralaimejai")
else:
    print("Laimejai")

print(skaiciai)
