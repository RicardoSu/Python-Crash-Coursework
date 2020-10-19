my_list = ('19','17','21','23')
new_list = enumerate(my_list)

for i in my_list:
	print(i)
	if i == '21':
		print(f'Now you can drink!')
	elif i > '21':
		print(f'You can drink!')
	elif i < '20':
		print(f'You cannot drink')

if '19' in my_list:
	print('19 is on the list')

if '1' is not my_list:
	print('you forgot 1')

x = 8

if x>0 and x<21:
	print('The number is less than 21')

if x>21 or x<21:
	print('X is a number')