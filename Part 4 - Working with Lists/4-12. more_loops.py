my_foods = ['pizza','falafel','carrot cake']
friends_food = my_foods[:]

for i in my_foods:
	print(i)

for i in friends_food:
	print(i)

print(set(my_foods) & set(friends_food))