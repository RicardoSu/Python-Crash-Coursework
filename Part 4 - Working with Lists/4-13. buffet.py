tokyo_menu = ('Edamame', 'GyozaTempura' , 'Fried shrimp' , 'Tatsuta' , 'AgeAge Tofu')
ordered_menu = enumerate(tokyo_menu)

for i,menu in ordered_menu:
	print(i+1,menu)


#tokyo_menu[0] ='Burger'

tokyo_menu = ('Fish Burguer', 'Baconator' , 'Fried shrimp' , 'Tatsuta' , 'AgeAge Tofu')
new_menu = enumerate(tokyo_menu)

for i,food in new_menu:
	print(i, food)