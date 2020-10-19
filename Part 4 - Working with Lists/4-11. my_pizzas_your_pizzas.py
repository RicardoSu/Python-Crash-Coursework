fav_pizza = ['Neapolitan Pizza','Chicago Pizza','New York-Style Pizza']

for pizza in fav_pizza:
	print(pizza)

for pizza in fav_pizza:
	if pizza == 'Neapolitan Pizza':
		print(f'I love {pizza}')
	elif pizza == 'Chicago Pizza':
		print(f'I want a {pizza} with extra cheeze!')
	elif pizza == 'New York-Style Pizza':
		print(f'{pizza} with coke, please.')

print(f'I love {fav_pizza[0]},{fav_pizza[1]},{fav_pizza[2]} I really love pizza.')

fav_pizza.append('Catupiri')
friend_pizza = ['Neapolitan Pizza','Chicago Pizza','New York-Style Pizza']
friend_pizza.insert(1,'Requizao')

for i in fav_pizza:
	print(i)
for i in friend_pizza:
	print(i)

print(set(fav_pizza) & set(friend_pizza))