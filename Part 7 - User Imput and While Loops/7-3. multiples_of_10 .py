number = input('Please input a number and I will tell you\
if it is a multiple of 10!')

if int(number) % 10 == 0:
	print(f"{number} it is a multiple of 10!")
else:
	print(f"{number} is not a multiple of 10")