age  = 'How old are you? Price goes by age.'
age += "\n(press 'q' to quit)"

active = True
current_number = 0

current_number += 1 

while active or current_number < 3:

	message = input(age)

	if message == 'q':
		active = False	
	elif int(message) < 3:
		print(f'You are {message} your ticket is free!')
		current_number += 1
		print('\n')
	elif int(message) >= 3 and int(message) <= 12:
		print(f'You are {message} your ticket is $10!')
		current_number += 1 
		print('\n')
	elif int(message) > 12 :
		print(f'You are {message} your ticket is $15!')
		current_number += 1 
		print('\n')
	elif message == 'q':
		break
	