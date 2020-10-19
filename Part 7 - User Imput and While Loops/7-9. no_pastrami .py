sawdwiches = ['Chicken Sandwich',
			'Pastrami'
			'Egg Sandwich',
			'Fish Sandwich',
			'Pastrami'			
			'Fried Egg Sandwich',
			'Grilled Cheese Sandwich'
			'Pastrami'
]

finished_sandwichs = []

print("The deli run out of pastrami")
while 'Pastrami' in sawdwiches:
	sawdwiches.remove('Pastrami')

while sawdwiches:

	finished = sawdwiches.pop()
	print(f'I made your {finished}')
	finished_sandwichs.append(finished)


print(sawdwiches)
print(finished_sandwichs)

for finished_sandwich in reversed(finished_sandwichs):
	print(f'Take your {finished_sandwich}')
	finished = finished_sandwichs.pop()
	sawdwiches.append(finished)
	
print(finished_sandwichs)
print(sawdwiches)