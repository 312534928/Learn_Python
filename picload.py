import pickle
f=open('hello.txt','rb')
d=pickle.load(f)
f.close()
print(d)