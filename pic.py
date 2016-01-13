import pickle
d=dict(name='Leon',age=23,score=99)
f=open('hello.txt','wb')
pickle.dump(d,f)
f.close()

f=open('hello.txt','rb')
d=pickle.load(f)
f.close()
print(d)