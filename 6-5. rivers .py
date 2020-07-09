rivers = {'Ucayali':'Peru','Amazon':'Brazil','Nile':'Africa'}

for key, value in rivers.items():
	print(f'The river {key.title()} is located in {value.title()}')
	print(key)
	print(value)