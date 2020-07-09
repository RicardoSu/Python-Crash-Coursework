usernames = [
]

for names in usernames:
	if not usernames:
		print('We need to find users!')
	elif names == 'admin':
		print('Hello admin yould you like a report status?')
	else:
		print(f'Hello {names}, thanks for logging again.')