class Animal(object):
	def run(self):
		print('Animal is running...')

class Dog(Animal):
	pass

class Cat(Animal):
	pass


dog=Dog()
dog.run()

cat=Cat()
cat.run()

print(isinstance(dog, Dog))
print(isinstance(dog, Animal))
print(isinstance(dog, Cat))


def run_twice(animal):
	animal.run()
	animal.run()

run_twice(Animal())

class Tortoise(Animal):
	def run(self):
		print('Tortoise is running slowly...')

run_twice(Tortoise())

print(type(dog))
print(isinstance([1, 2, 3], tuple))
