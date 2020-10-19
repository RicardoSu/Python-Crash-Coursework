def city_functions(city,country):
	"""Function that returns a string with the values"""
	functions = f"{city},{country}"
	return functions.title()

import unittest
from city_functions import city_functions

class Testcity_functions(unittest.TestCase):
		def test_city_country(self):
			formated_name = city_functions('macapa','amapa')
			self.assertEqual(formated_name,'Macapa,Amapa')