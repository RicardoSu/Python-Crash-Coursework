table = input('How many people to be seated? ')
while True:
	try:
		if table >= '8':
			print('Please wait')
			break
		elif table > '0' and table < '8':
			print('Your table is ready!')
			break
		else:
			print('Invalid number')
			break
	except ValueError:
	 	print ("Please use only numbers")
	 	break
	