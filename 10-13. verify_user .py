import json


def get_stored_username():
	'''Get stored username if available'''
	filename = 'username.json'
	try:
		with open (filename) as f:
			username = json.load(f)

	except FileNotFoundError:
		return None
	else:
		return username

def get_new_username():
	'''Prompt a new username'''
	username = input('What is your username?')
	filename = 'username.json'
	with open (filename,'w') as f:
		json.dump(username,f)

def greet_user():
	'''Greet user by name'''
	username = get_stored_username()
	returning_user = input(f'Are you {username} ? (Please Enter Y/N)')
	if returning_user == 'Y':
		print(f'Welcome back {username}')
	else:
		username = get_new_username()
		print(f"We'll remember you when you come back")

greet_user()