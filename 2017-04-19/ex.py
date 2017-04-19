

class Time:

	def __init__(self, h, m, s):
		self.h = h
		self.m = m
		self.s = s
		assert self.is_valid()

	def dump(self):
		print("Time: h=", self.h, "m=", self.m, "s=", self.s)

	def is_valid(self):
		if self.h<0 or self.h > 23:
			return False
		if self.m < 0 or self.m > 59:
			return False
		if self.s < 0 or self.s > 59:
			return False
		return True

	def add_seconds(self, sec):
		self.add_minutes(sec/60)
		self.s += int(sec % 60)
		
	def add_hours(self, h):
		self.h += int(h % 24)

	def add_minutes(self, m):
		h = m / 60
		self.add_hours(h)
		self.m += int(m % 60)


t = Time(1, 22, 15)

t.dump()
print(t.is_valid())


# t = Time(55, 155, 305)
t.add_seconds(3600)
t.dump()
print(t.is_valid())

t.add_minutes(3600)
t.dump()
print(t.is_valid())




