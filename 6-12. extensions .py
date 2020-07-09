favorite_lanuages = {
	'jen':['python','ruby'],
	'sarah':['c'],
	'edward':['ruby','go'],
	'phil':['pyhton','haskell']
}

for key,values in favorite_lanuages.items():
	if len(values) > 1:
		print(f"{key.title()}'s favorite languages are:")
	elif len(values) == 1:
		print(f"{key.title()}'s favorite language is:")
	for value in values:
		print(f"\t {value.title()}")