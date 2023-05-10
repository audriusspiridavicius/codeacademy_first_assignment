import copy
import random

l = [1, 2, 3, 4, -10, 100, {"vardas" : "jonas"}]

dic = {
    "Amzius" : 30,
    "Vardas" : "Audrius",
    "email" : "audriusspiridavicius@gmail.com"
}

print(f"mano vardas - {dic['Vardas']}")
print(f"siaip skaicius {l[random.randint(0,len(l)-1)]}")


l.append(11.5)
dic["age123"] = 30

print(f"mano vardas - {dic['age123']}")
print(f"siaip skaicius {l[random.randint(0,len(l)-1)]}")


del_l = l.pop(0)
del_dict = dic.pop("Amzius")
print(l)
print(dic)

dic["Amzius"] = del_dict

print(dic)

print(l)
# new_list = l this works not the way i want
new_list = copy.deepcopy(l)
print(f"new list = {new_list}")
new_list[0] = -99999
new_list[-2]["vardas"] = "petriukas"
print(f"new list = {new_list}")
print(l)
