guest_list = ['Michael Jackson' , 'Elvis Presley' , 'Charles Schulz' , 'Bob Marley']
my_name = 'Ricardo'

guests = enumerate(guest_list)

print(f'{guest_list[0]} cannot make to the dinner.')

guest_list[0] = 'John Lennon'

for i,guest in guests:
	print(f'{guest} I would like to invite cordially for dinner -{my_name}')