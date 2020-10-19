import json

number = input('Whats is your favorite number?')
numbers = [number]

filename = 'numbers.json'

with open (filename,'w') as f:
	json.dump(numbers,f)