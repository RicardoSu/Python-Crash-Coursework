def sandwiches(*toppings):
	print(f'Making a pizza with the following toppings:')
	for top in toppings:
		print(f'\t{top}')



sandwiches('rice','beans','fries')