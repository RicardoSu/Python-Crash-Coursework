class Restaurant():

	def __init__(self,restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		print(f'The restaurant name is {self.restaurant_name} and the cuisine type {self.cuisine_type}.')
	def open_restaurant(self):
		print('The restaurant is open')	


restaurant = Restaurant('Sushi Bar','Japanese')
restaurant2 = Restaurant('Tofu','Chinese')
restaurant3 = Restaurant('Churrasco','Brazil')

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()