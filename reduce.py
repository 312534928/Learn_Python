from functools import reduce
def add(x,y):
	return x+y

a=reduce(add,[1,3,5,7,9])
print(a)

def fn(x,y):
	return x*10+y

b=reduce(fn,[1,3,5,7,9])

print(b)