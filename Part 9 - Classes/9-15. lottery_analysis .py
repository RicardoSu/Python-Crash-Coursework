from random import randint
import random
import string

class Lottery():
	def __init__(self,lotto_number = 1):
		self.lotto_number = lotto_number

	def lotto_numbers(self):
		randon_letter = random.choice(string.ascii_lowercase)
		return randint(1,self.lotto_number),random.choice(string.ascii_lowercase)

ticket = Lottery(2)

winning_numbers = []

ticket1 = [(1, 'a')]





run = True
times_running = 0
while run:
	if ticket1 == [ticket.lotto_numbers()]:
		print('Winnin Ticket!')
		run = False
	else:
		print(ticket.lotto_numbers())
		times_running += 1
		print(f'Tickets {times_running}')


