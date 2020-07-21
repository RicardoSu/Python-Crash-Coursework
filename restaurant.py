class Restaurant():

	def __init__(self,restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		print(f'The restaurant name is {self.restaurant_name} and the cuisine type {self.cuisine_type}.')

	def open_restaurant(self):
		print('The restaurant is open')

	def restaurant(self):
		print(f'The restaurant has served {self.number_served} custumers')



	def cust_served(self, number):

		if number >= self.number_served:
			self.number_served = number
		else:
			print(f'You cant reduce this list')

	def increment_cust(self,new_number):
		self.number_served += new_number




