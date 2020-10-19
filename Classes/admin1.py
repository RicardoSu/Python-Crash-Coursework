from user1 import User

class Admin(User):
	def __init__(self,first_name,last_name):
		super().__init__(first_name,last_name)
		self.privileges = Priviledges([])
class Priviledges():
	def __init__(self,privileges = []):
		self.privileges = privileges

	def show_privileges(self):
		if self.privileges:

			for privilege in self.privileges:
				print(privilege)
		else:
			print(f'You have no privileges')

