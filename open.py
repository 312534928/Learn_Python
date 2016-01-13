import os
print(os.getcwd())

f=open('hello.txt')
for line in f.readlines():
	print(line.strip())

f.close()