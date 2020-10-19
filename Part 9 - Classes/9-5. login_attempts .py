class User:
	def __init__(self,first_name,last_name):
		self.first_name = first_name
		self.last_name = last_name
		self.attempts = 0

	def describe_user(self):
		print(f'Full name: {self.first_name} {self.last_name}')

	def greet_user(self):
		print(f'Hello {self.first_name}!')

	def login_attempts(self):
		print(f'Attempt number {self.attempts}')

	def increment_login_attempts(self):
		self.attempts += 1

	def reset_login_attempts(self):
		self.attempts = 0

	def add_login_attempts(self,number):
		self.attempts += number

user1 = User('Mario','Armario')
user1.login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.login_attempts()
user1.add_login_attempts(5)
user1.login_attempts()


