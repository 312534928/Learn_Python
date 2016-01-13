'''
__getattr__ 拦截属性点号运算
'''
class Student(object):
	def __init__(self, name):
		self.name = name

	def __getattr__(self, attr):
		if attr == 'score':
			return 99
		raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)


s = Student('Leon')
print(s.name)
print(s.score)
# print(s.age)
