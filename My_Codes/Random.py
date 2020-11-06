import random

drange=[1,2,3,4,5,6]

class Dice:
	def Roll(self):
		return random.choice(drange)



d1=Dice()
d2=Dice()
print((d1.Roll(),d2.Roll()))

