favorite_lanuages = {
	'jen':'python',
	'sarah':'c',
	'edward':'ruby',
	'phil':'pyhton'
}

pool_list = ['mario','phil','kevin']

#polled_list = enumerate(favorite_lanuages)

for pool in pool_list:
	if pool in favorite_lanuages.keys():
		print(f'user {pool} already took the test')
	elif pool is not favorite_lanuages.keys():
		print(f'user {pool} please take the test')


