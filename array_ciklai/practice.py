import copy
import random

a = [1,2,3]
b = a

b[0] = 10
print(a)
print(b)


c = [1,2,3]
d = c

d[0] = 10
print(c)
print(d)


t = ([0],[1])
print(t)

t[0][0] = 100
t[1][0] = 100
print(t)
