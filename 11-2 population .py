def city_functions(city,country,population=""):
	"""Function that returns a string with the values"""
	
	if population:
		functions = f"{city},{country},Population:{population}"

	else:
		functions = f"{city},{country}"
	return functions.title()

import unittest
from city_functions import city_functions

class Testcity_functions(unittest.TestCase):
	'''Does cities with population works?'''
	def test_city_country(self):
		formated_name = city_functions('amapa','macapa','500')
		self.assertEqual(formated_name,'Amapa,Macapa,Population:500')