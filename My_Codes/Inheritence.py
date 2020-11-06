class Mammals:
	def walk(self):
		print('walk')

class Dog(Mammals):
	pass

class Cat(Mammals):
	def meow(self):
		print('meow')


dog1=Dog()
cat1=Cat()
dog1.walk()
cat1.meow()
cat1.walk()