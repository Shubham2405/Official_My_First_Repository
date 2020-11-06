class Point:
	def move(self):
		print('move')

	def draw(self):
		print('draw')

point1=Point()
point1.x=3
point1.y=7
print(point1.x)
print(point1.y)
point2=Point()
point2.x=4
point1.draw()
# We use classes to define new types.
# Types can have method which we define in the body of the class.
#  And they can also have attributes which we can set anywhere in our program.
