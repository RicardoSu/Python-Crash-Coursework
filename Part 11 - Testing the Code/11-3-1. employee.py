class Employee(object):
	"""docstring for ClassName"""
	def __init__(self, first,last,salary):
		self.first = first
		self.last = last
		self.salary = salary

	def give_raise(self,amount=5000):
		self.salary += amount

import unittest
from employee import Employee

class test_Employee(unittest.TestCase):
	def setUp(self):
		self.mario = Employee('mario','armario',5)
	def test_give_default_raise(self):
		self.mario.give_raise()
		self.assertEqual(self.mario.salary,5005)
	def test_give_custom_raise(self):
		self.mario.give_raise(4000)
		self.assertEqual(self.mario.salary,4005)
unittest.main()