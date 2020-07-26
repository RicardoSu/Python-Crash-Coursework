import unittest
from city_functions import city_functions

class Testcity_functions(unittest.TestCase):
		def test_city_country(self):
			formated_name = city_functions('macapa','amapa')
			self.assertEqual(formated_name,'Macapa,Amapa')