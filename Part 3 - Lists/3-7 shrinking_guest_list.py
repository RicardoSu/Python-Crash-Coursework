guests = ['Whitney Houston', 'John Lennon', 'Marilyn Monroe', 'Elvis Presley',
'Charles Schulz', 'Bob Marley', 'Jimi Hendrix']

print('Sorry guys only 2 poeple can be with me')

new_list = enumerate(guests)
count = len(guests)


while 2 < count:
	eliminated = guests.pop()
	print(f'Sorry {eliminated} only 2 people on the table')
	count -= 1

for i,guest in new_list:
	print(f'Hey, {guest} you still invited to the dinner')