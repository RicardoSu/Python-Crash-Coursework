filename = 'learning_python.txt'


with open (filename) as file_object:
	contents = file_object.read()
	print(contents)

with open (filename) as file_object:
	for file in file_object:
		print(f'{file.rstrip()}')

with open (filename) as file_object:
	new_files = file_object.readlines()
	for new_file in new_files:
		print(new_file.rstrip())
