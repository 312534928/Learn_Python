class Student(object):
	def __init__(self, name,score):  ##第一个参数永远是self
		self.name = name
		self.score = score
	def print_score(self):
		print('%s:%s'%(self.name, self.score))
	def get_grade(self):
		if self.score>=90:
			return 'A'
		elif self.score>=60:
			return 'B'
		else:
			return 'C'

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()


def printOut(std):
	print('%s:%s' %(std.name, std.score))

printOut(bart)

print(lisa.get_grade())