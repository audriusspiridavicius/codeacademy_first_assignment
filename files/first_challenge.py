import datetime
import os

text = """The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

with open("text-file.txt", "w") as tfile:
    tfile.write(text)


# with open("text-file.txt", "r") as file:
#     textas = file.read()
#     print(textas)
#
#
with open("text-file.txt", "a") as file:
    #file.read()
    file.write(f"\n{datetime.datetime.now()}")
lines =[]
with open("text-file.txt","r") as file:
    lines = file.readlines()

lines = [line.replace("Beautiful is better than ugly.", "Gražu yra geriau nei bjauru.") for line in lines]
lines = [f"{index + 1} {line}" for index, line in enumerate(lines)]

with open("text-file.txt","w") as file:
    file.writelines(lines)

with open("text-file.txt","r") as file:
    lines = file.readlines()


with open("text-file.txt","r") as file:
    text_from_file = file.read().replace('\n', '')

    text_words = len(text_from_file.split())
    number_count = len([symbol for symbol in text_from_file if symbol.isdigit()])
    uppercase_count = len([symbol for symbol in text_from_file if symbol.isupper()])
    lowercase_count = len([symbol for symbol in text_from_file if symbol.islower()])
    print(f"number_count = {number_count}")
    print(f"uppercase_count = {uppercase_count}")
    print(f"lowercase_count = {lowercase_count}")
    print(f"words count = {text_words}")

    print(lines)

lines.reverse()
#print(lines)


with open("text-file.txt", "r") as read_file:
    with open("text-file2.txt", "w") as write_file:
        for read_file_line in read_file:
            write_file.write(read_file_line.upper())




