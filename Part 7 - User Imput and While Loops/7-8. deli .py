sawdwiches = ['Chicken Sandwich',
			'Egg Sandwich',
			'Fish Sandwich',
			'Fried Egg Sandwich',
			'Grilled Cheese Sandwich'
]

finished_sandwichs = []

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