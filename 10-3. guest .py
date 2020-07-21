filename = 'guest.txt'

names = input('Whats is your name?')

with open(filename,'w') as f:
	f.write(names)