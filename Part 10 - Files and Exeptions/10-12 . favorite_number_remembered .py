import json

while True:	
	number = input('Whats is your favorite number?')
	numbers = [number]
	
	filename = 'numbers.json'
	
	with open (filename,'w') as f:
		json.dump(numbers,f)
	

	with open (filename) as f:
		numbers = json.load(f)
	for number in numbers:
		fav_number = number
	
	print(f'Your favorite number is {fav_number}')
	
