


import os


print(os.getcwd())


cwd = os.getcwd()

filename = os.path.join(cwd, 'ex.py')
print(filename)

home = os.path.expanduser('~')

print(home)

home = os.path.expanduser('~lubo')
print(home)


filename = os.path.join(
	os.path.expanduser('~'),
	'School',
	'python2016-2017',
	'2017-03-01',
	'ex.py')

print(filename)

print(os.path.split(filename))
wd, filename = os.path.split(filename)
print(wd, filename)


t = ('a', 'b')
(v, u) = t
print(v, u)

print(filename)
print(os.path.splitext(filename))




import glob

print(glob.glob('*l*'))

allfiles = glob.glob('*')
print(allfiles)

for f in allfiles:
	print(f)



l = [1,2,3,4,5]
res = []
for v in l:
	res.append(2*v)
print(res)


res = l

res = [v for v in l]
print(res)

res =[2*v for v in l]
print(res)


res = [2*v for v in l if v%2 == 0]
print(res)



res = [os.path.join(cwd,v) for v in glob.glob("*") if 'py' not in v]
print(res)



res = {'k'+str(v):v for v in l}
print(res)

print(res.keys())
print(res.values())

for k,v in res.items():
	print(k,v)

print(res.items())

for t in res.items():
	k,v = t
	print(k,v)


for k in res:
	print(k, res[k])
	
for v in res.values():
	print(v)


res = {str(v):v for v in l}
print(res)

d = {k + k:2*v for k,v in res.items()}
print(d)


s = {k + str(2*v) for k,v in res.items()}
print(s)









