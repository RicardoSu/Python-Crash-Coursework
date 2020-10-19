  
while True:
	a = input('Enter a number to add:')
	b = input('Enter second number to add:')
	suma = (int(a) + int(b))
	message = 'Please input a number'
	try:
		print(f'Result:{suma}')

	except ValueError:
		print(message)

