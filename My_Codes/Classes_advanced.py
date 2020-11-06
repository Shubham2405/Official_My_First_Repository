class Point:
	def __init__(self,a,b):
		self.x=a
		self.y=b

	def write(self):
		print('write')

	def move(self):
		print('move')

origin=Point(5,4)
print(origin.x)
origin.x=0
print(f'x is {origin.x} and y is {origin.y}')
origin.write()

#This program is completed now next is excercise.


class Person:
	def __init__(self,a):
		self.name=a

	def talk(self):
		print(f'{self.name} is talking !')


chot=Person('Yash')
print(chot.name)
chot.talk()
chot.name='bilota'
print(chot.name)
chot.talk()