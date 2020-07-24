file = 'poll.txt'

while True:

	with open(file,'a') as f:

		poll_input = input('Why do you like programming?')
		f.write(poll_input + '\n')

		survey = input('Would you like someone else take the survey? Y/N')

		print(survey)

		if survey == 'N':
			break
