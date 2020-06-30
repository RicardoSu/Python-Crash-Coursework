responses = {}
polling_active = True

while polling_active:
	name = input("What is your name?")
	location = input(f'{name.title()} where would you like to travel?')

	responses[name] = location
	print(responses)

	another = input('Would you like to travel with someone else?  (yes/no)')
	if another == 'no':
		polling_active = False

print('--------Results---------')
for name, location in responses.items():
	print(f'{name.title()} would love to travel to {location.title()}')




