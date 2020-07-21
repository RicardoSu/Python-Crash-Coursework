from User import User,Admin,Priviledges

user1 = Admin('mario','armario')

user1.describe_user()

user1_privileges = ['can add a post',
	 'can delete a post',
	'can ban user'
]

user1.privileges.privileges = user1_privileges
user1.privileges.show_privileges()