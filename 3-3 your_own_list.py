love_cars = [' because it protects me.', ' because it comforts me.',
	' because it gives me freedom to move.']
love_motorcycles = ['I can Find my Zen', 'Commuting Is Easier And More Fun',
	'You Learn About Perspective']

car = 0
len_car = (len(love_cars) - 1)
while car <= len_car :
	print(f'I love my car because{love_cars[car]}')
	car += 1

motorcycles = 0 
len_motorcycles = len(love_motorcycles) - 1

while motorcycles <= len_motorcycles:
	print(f'I love my motorcycle because {love_motorcycles[motorcycles]}')
	motorcycles += 1