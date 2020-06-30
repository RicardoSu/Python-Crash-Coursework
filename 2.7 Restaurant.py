class Restaurant:
	""" Docstring for Restaurant"""
	def __init__(self,restaurant_name,cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		print(f"Restautant Name is {self.restaurant_name} our specialty is {self.cuisine_type}")

	def open_restaurant(self):
		print(f"{self.restaurant_name} is now open")
 


restaurant = Restaurant('Maria Magdallena','Feijoada')


print(f"We love {restaurant.cuisine_type}")
restaurant.describe_restaurant()