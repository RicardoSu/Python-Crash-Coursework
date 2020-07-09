age  = 'How old are you? Price goes by age.'
age += "\n(press 'q' to quit)"

active = True

while active:

	message = input(age)

	if message == 'q':
		active = False	
	elif int(message) < 3:
		print(f'You are {message} your ticket is free!')
		print('\n')
	elif int(message) >= 3 and int(message) <= 12:
		print(f'You are {message} your ticket is $10!')
		print('\n')
	elif int(message) > 12 :
		print(f'You are {message} your ticket is $15!')
		print('\n')
	