filename = 'learning_python.txt'


with open (filename) as file_object:
	
	for file_objects in file_object:
		new_line = file_objects.rstrip().replace('python','C')
		print(new_line)



