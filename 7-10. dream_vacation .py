anwsers = {}

while True:
	name = input('What is your name?')
	place = input('Where yould you like to travel?')

	anwsers[name] = place

	repeat = input('Would you like soeone else to take\
the pool? (yes/no)')
	if repeat == 'no':
		break

for key,value in anwsers.items():
	print(f"{key.title()},would love to visit {value.title()}")