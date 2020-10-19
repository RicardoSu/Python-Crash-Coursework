filenames = ['dogs.txt', 'cats.txt']

for file in filenames:
	print(f'File name: {file}\n')
	try:
		with open(file) as f:
			read_file = f.read()
			print(read_file)
	except FileNotFoundError:
		print('File is missing')
