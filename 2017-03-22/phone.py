import re

PHONES = [
	'800-555-1212',
	'800 555 1212',
	'800.555.1212',
	'(800) 555-1212',
	'1-800-555-1212',
	'800-555-1212-1234',
	'800-555-1212x1234',
	'800-555-1212 ext. 1234',
	'work 1-(800) 555.1212 #1234',
]


phones = r'^$'


for p in PHONES:
	m = re.match(phones, p)
	if m is None:
		print("cant match: ", p)

		
