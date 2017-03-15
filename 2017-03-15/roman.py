

import re


s = 'MMMM'


pattern = r'^MMMM$'

m = re.match(pattern, s)
print(m.group(0))

s = 'MM'
m = re.match(pattern, s)
print(m)


pattern = r'^M?M?M?M?$'
print(re.match(pattern, 'MM'))
print(re.match(pattern, 'MMMM'))
print(re.match(pattern, ''))
print(re.match(pattern, 'MMMMM'))

pattern = r'^M*'
print(re.match(pattern, 'MM'))
print(re.match(pattern, 'MMMMM'))
print(re.match(pattern, ''))


print(re.match(r'^M+$', 'MMMMMM'))
print(re.match(r'^M+$', ''))



HUNDREDS = [
	'C',
	'CC',
	'CCC',
	'CD',
	'D',
	'DC',
	'DCC',
	'DCCC',
	'CM',
]

print(HUNDREDS)


pattern = r'^(C{1,3}|CD|CM|DC{0,3})$'

for s in HUNDREDS:
	print(re.match(pattern, s))


TENS = [
	'X',
	'XX',
	'XXX',
	'XL',
	'L',
	'LX',
	'LXX',
	'LXXX',
	'XC',
]

p10 = r'^(X{1,3}|XL|XC|LX{0,3})$'

for s in TENS:
	print(re.match(p10, s))


ROMANS = [
	'MDCCLXX',
]

pattern = r'^(M+)?(C{1,3}|CD|CM|DC{0,3})?(X{1,3}|XL|XC|LX{0,3})?$'


for s in ROMANS:
	print(re.match(pattern, s))



pattern = '''
^							#
(M+)?						# matches thousands
(C{1,3}|CD|CM|DC{0,3})?		# matches handreds
(X{1,3}|XL|XC|LX{0,3})?		#
$							#
'''


for s in ROMANS:
	print(re.match(pattern, s, re.VERBOSE))



