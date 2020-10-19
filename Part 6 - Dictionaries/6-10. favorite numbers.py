fav_numbers = {
				'Liam':['21','16'], 
				'Emma':'3', 
				'Noah':'6', 
				'Olivia':['7','14'], 
				'William':'3'
}

for key,values in fav_numbers.items():
	if len(values) > 1:
		print(f'{key} favorite numbers are:')
	elif len(values) == 1:
		print(f'{key} favorite number is:')
	for value in values:
		print(value, end=' ')
		print('\n')