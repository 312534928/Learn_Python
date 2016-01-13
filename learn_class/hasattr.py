class MyObject(object):
	def __init__(self):
		self.x = 9

	def power(self):
		return self.x * self.x


obj = MyObject()

print(hasattr(obj, 'x'))
print(getattr(obj, 'y', 404))
