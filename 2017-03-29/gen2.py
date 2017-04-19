


def gen():
	print("before 1")
	yield 1
	print("before 2")
	yield 2
	print("before 3")
	yield 3
	print("after 3")



g = gen()

"""
print(next(g))

print(next(g))

print(next(g))

print(next(g))
"""

for v in g:
	print(v)

