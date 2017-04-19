
class Point:
	
	def __init__(self, x, y):
		print("Point() constructor called...")
		self.x = x
		self.y = y
	
	def dump(self):
		print("P(", self.x, ",", self.y, ")")

	def move_x(self, dx):
		self.x = self.x + dx

	def move_y(self, dy):
		self.y = self.y + dy

	def move(self, dx, dy):
		self.x += dx
		self.y += dy

	def __eq__(self, other):
		print("Point.__eq__ called...")
		return self.x == other.x and self.y == other.y

	

p0 = Point(0,0)
p0.dump()

p1 = Point(1,1)
p1.dump()

print(p0.x)
print(p1.y)


p0.move_x(10)
p0.dump()
p0.move_y(10)
p0.dump()


p1.move(10,10)
p1.dump()

print(p1 == p0)


p0.move(1,1)
print(p1 == p0)

