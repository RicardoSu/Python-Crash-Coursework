usernames = ['username', 'administrator', 
			'Administrator', 'user1',
			'admin', 'alex'
]

new_users = ['mario', 'alex', 
			 'ben', 'admin', 
			 'rose'
]


new_users = [user.lower() for user in new_users]

for users in new_users:
	if users in usernames:
		print(f'Username {users} is current in use')
	else:
		print(f'Cool your username is availabe! {users}')