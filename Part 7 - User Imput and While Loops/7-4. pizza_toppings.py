prompt = 'Please enter the pizza topping that you like:'
prompt += '\n(enter "quit" to quit)'

active = True

while active:
	message = input(prompt)

	if message == 'quit':
		active = False
	else:	
		print(f'Adding {message} to your pizza')


