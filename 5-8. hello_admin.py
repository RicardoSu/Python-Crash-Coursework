usernames = ['username', 'administrator', 
			'Administrator', 'user1',
			'admin', 'alex'
]

for names in usernames:
	if names == 'admin':
		print('Hello admin yould you like a report status?')
	else:
		print(f'Hello {names}, thanks for logging again.')