


class Reverse:
	"""
	Creates reverse sequence of integers.
	"""

	def __init__(self, n):
		self.n = n
	
	def __iter__(self):
		return self
		
	def __next__(self):
		self.n = self.n - 1
		if self.n < 0:
			raise StopIteration()

		return self.n
		
r = Reverse(5)

for i in r:
	print(i)


print(r.__class__)
print(r.__doc__)


