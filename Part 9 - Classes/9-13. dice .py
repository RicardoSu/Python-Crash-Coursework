from random import randint

class Dice():

	def __init__(self,sides = 6):
		self.sides = sides

	def roll_dice(self):
		return randint(1, self.sides)	

d12 = Dice(8)
	
print(Dice(8).roll_dice())

results = []

for rools in range(10):
	result = d12.roll_dice()
	results.append(result)
print(results)
