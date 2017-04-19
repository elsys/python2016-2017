



def fun(v):
	print("calling fun() with value v=", v)
	return 2*v


# print(fun(1))


def gen(maxv):
	while maxv > 0:
		print("before yield")
		yield fun(maxv)
		maxv -= 1

g = gen(3)


print(next(g))
# print(next(g))

"""
for v in g:
	print(v)
"""

