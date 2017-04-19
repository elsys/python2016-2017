

class Date:
	DAYS_IN_MONTH = [
		-1, 
		31, 28, 31, 30, 
		31, 30, 31, 31, 
		30, 31, 30, 31]

	def __init__(self, y, m, d):
		self.y = y
		self.m = m
		self.d = d
		assert self.is_valid()

	def is_valid(self):
		if self.y < 1000 or self.y > 2200:
			return False
		if self.m < 1 or self.m > 12:
			return False
		if self.d < 1 or self.d > self.DAYS_IN_MONTH[self.m]:
			return False
		return True

	def dump(self):
		print("Date: y=%d; m=%d; d=%d" % (self.y,self.m,self.d))

	def is_leap_year(self):
		if self.y % 4 != 0:
			return False
		elif self.y % 100 != 0:
			return True
		elif self.y % 400 != 0:
			return False
		else:
			return True

"""
d = Date(2016, 4, 19)
d.dump()
print(d.is_leap_year())

d = Date(2017, 2, 28)
d.dump()
print(d.is_leap_year())

d = Date(1900, 1, 1)
d.dump()
print(d.is_leap_year())

d = Date(2000, 1, 1)
d.dump()
print(d.is_leap_year())
"""


import unittest

class DateTest(unittest.TestCase):


	def test_leap_year(self):
		print("test_leap_year() called...")
		d = Date(2000, 1, 1)
		self.assertTrue(d.is_leap_year())

	def test_construct_good(self):
		d = Date(2000, 1, 1)
		self.assertEqual(d.y, 2000)
		self.assertEqual(d.m, 1)
		self.assertEqual(d.d, 1)

	def test_construct_bad(self):
		with self.assertRaises(AssertionError):
			Date(0, 1, 1)
		with self.assertRaises(AssertionError):
			Date(2000, 0, 1)


	

"""
	def test_leap_year_bad(self):
		print("test_leap_year() called...")
		d = Date(2001, 1, 1)
		self.assertTrue(d.is_leap_year())
"""
	
	
unittest.main()


