guest_list = ['Michael Jackson' , 'Elvis Presley' , 'Charles Schulz' , 'Bob Marley']
my_name = 'Ricardo'

guests = enumerate(guest_list)

for i, guest in guests:
	print(f'{i} Dear {guest} I would like to invite cordially for dinner -{my_name}')