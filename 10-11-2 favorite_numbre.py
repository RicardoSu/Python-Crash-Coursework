import json

filename = 'numbers.json'

with open (filename) as f:
	numbers = json.load(f)
for number in numbers:
	fav_number = number

print(f'Your favorite number is {fav_number}')

