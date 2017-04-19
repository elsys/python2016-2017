


def gen(maxv):
	while maxv > 0:
		yield maxv
		print("after yield")
		maxv -= 1


g = gen(3)

"""
print(next(g))
print(next(g))
print(next(g))
"""

for v in g:
	print(v)




