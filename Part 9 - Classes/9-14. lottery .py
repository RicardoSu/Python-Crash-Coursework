from random import randint
import random
import string

class Lottery():
	def __init__(self,lotto_number = 1):
		self.lotto_number = lotto_number

	def lotto_numbers(self):
		randon_letter = random.choice(string.ascii_lowercase)
		return randint(1,self.lotto_number),random.choice(string.ascii_lowercase)

ticket = Lottery(8)

winning_numbers = []


for numbers in range(1):
	result = ticket.lotto_numbers()
	winning_numbers.append(result)

print(winning_numbers)



