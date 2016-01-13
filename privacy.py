class Student(object):
	def __init__(self, name, score):  # 第一个参数永远是self
		self.__name = name
		self.__score = score

	def print_score(self):
		print('%s:%s' % (self.__name, self.__score))

	def get_name(self):
		return self.__name

	def get_score(self):
		return self.__score

	def set_score(self, score):
		if 0 <= score <= 100:
			self.__score = score
		else:
			raise ValueError('bad score')


class Student1(object):
	def __init__(self, name, score):  # 第一个参数永远是self
		self.name = name
		self.score = score

	def print_score(self):
		print('%s:%s' % (self.name, self.score))


Leon1 = Student1('Leon1', 98)

print(Leon1.score)

Leon = Student('Leon', 98)
print(Leon.get_score())

Leon.set_score(88)
print(Leon.get_score())

Leon.set_score(101)
print(Leon.get_score())

# print(Leon.__name)
# print(Leon._Student__name)
print(Leon.get_name())
