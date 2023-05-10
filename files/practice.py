import os


print(os.getcwd())

os.chdir("C:/Users/User/Desktop")
print(os.getcwd())

print(os.listdir())
os.chdir("C:/Users/User/PycharmProjects/codeacademy_first_assignment/files")
print(os.getcwd())
print(os.listdir())
os.mkdir("test aplankas")
print(os.listdir())