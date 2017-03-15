

s = '100 NORTH MAIN ROAD'
res = s.replace('ROAD', 'RD.')

print(res)


s = '100 NORTH BROAD ROAD'
print(s)
res = s.replace('ROAD', 'RD.')

print(res)


import re

print(re.sub('ROAD', '\tRD.', s))

print(re.sub('ROAD$', 'RD.', s))


s = '100 BROAD'
print(re.sub('\\bROAD$', 'RD.', s))

s = '100 BROAD ROAD'
print(re.sub('\\bROAD$', 'RD.', s))


print(re.sub(r'\bROAD$', 'RD.', s))


s = '100 BROAD ROAD APT. 3'
print(re.sub(r'\bROAD\b', 'RD.', s))
 
