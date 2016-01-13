import copy
a=10
b=a
a=11
print(b)

c=copy.copy(a)
print(a," ",c)
a=12
print(a," ",c)

c=copy.deepcopy(a)
print(a," ",c)
a=13
print(a," ",c)