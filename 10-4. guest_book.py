filename = 'guest.txt'



while True:
	names = input('Whats is your name? (enter "q" to close)')
	if names == 'q':
		break
	else:
		with open(filename,'a') as f:
			f.write(names + '\n')
		print(f'Hello {names} you have been added to the guest book.')