import json
 
class Student(object):
	def __init__(self,name,age,score):
		self.name=name
		self.age=age
		self.score=score

s=Student('Leon',23,99)

def student2dict(std):
	return{
	'name':std.name,
	'age':std.age,
	'score':std.score
	}
a=json.dumps(s,default=student2dict)
print(a,type(a))

def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

b=json.loads(a,object_hook=dict2student)
print(b,type(b))