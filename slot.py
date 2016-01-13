class Student(object):
	__slots__=('name','score')

s=Student()
s.name='Leon'
print(s.name)

def set_age(self,age):
	self.age=age

from types import MethodType
s.set_age=MethodType(set_age,s) #给实例绑定一个方法
s.set_age(23)
print(s.age)


def set_score(self,score):
	self.score=score

Student.set_score=MethodType(set_score,Student)

s2=Student()
s2.set_score(99)
print(s2.score)
s.set_score(100)
print(s.name,'score:',s.score)

