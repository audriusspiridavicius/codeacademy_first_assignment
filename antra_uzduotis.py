full_name = "Spiridavicius Audrius"

# name = full_name[:7]
# lastname = full_name[7:]
name = full_name.split(" ")[0]
lastname = full_name.split(" ")[1]

print(f"my full name is {full_name}")
print(f"last symbol of my lastname is : {full_name[-1]}")
print(f"first symbol of my first name is : {full_name[0]}")
print(f"my name is {name}")
print(f"my surname is {lastname}")
print(f"my full name is {full_name.upper()}")
print(f"my full name(reversed) is {lastname} {name}")
print(f"my full name(reversed) is {full_name[::-1]}")

m_name = full_name.split(" ")
print(m_name)
full_name = full_name.replace(lastname, "Python Specialistas")
print(full_name)
