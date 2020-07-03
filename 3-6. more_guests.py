guest_list = ['Michael Jackson' , 'Elvis Presley' , 'Charles Schulz' , 'Bob Marley']
my_name = 'Ricardo'

guests = enumerate(guest_list)

guest_list[0] = 'John Lennon'

guest_list.insert(0, 'Whitney Houston')
guest_list.insert(int(len(guest_list)/2), 'Marilyn Monroe')
guest_list.append("Jimi Hendrix")

for i,guest in guests:
	print(f"I would like to invite {guest} cordially to our dinner -{my_name}")
