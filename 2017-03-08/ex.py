

s = "Здравейте на български"
print(s)

print(len(s))


SUFFIXES = {
	1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
	1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB'],
}

def approximate_size(size, a_kilobyte_is_1024_bytes=True):
	'''Convert a file size to human-readableform. 
	
    Keyword arguments:
    size -- file size in bytes
    a_kilobyte_is_1024_bytes -- if True (default), use multiples of 1024
                                if False, use multiples of 1000

    Returns: string
    '''     
	if size < 0:
		raise ValueError("unexpected size value")
	
	if a_kilobyte_is_1024_bytes:
		multiple = 1024
	else:
		multiple = 1000

	print("Multiple: ", multiple)

	for suffix in SUFFIXES[multiple]:
		size = size / multiple  # size /= mulitple
		if size < multiple:
			result = "{0:.1f} {1}".format(size, suffix)
			print(result)
			return result



approximate_size(1000000)
approximate_size(1000000, False)
approximate_size(1024, True)


print("{}/{}/{}".format(10, 3.14, "ala-bala"))
print("{2}/{0}/{1}".format(10, 3.14, "ala-bala"))


approximate_size(1)

# a = 1==2?1:2
	
suffixes = SUFFIXES[1000]
print(suffixes)


res = "1000{0[0]} = 1{0[1]}".format(suffixes)
print(res)

res = "{0} = {0}".format(['a', 'b'])
print(res)


res = "{0[0]} = {0[1]}".format(['a', 'b'])
print(res)




#

s = """aaaaa
bbbbbb
ccccccc
dddddddd"""
print(s)
res = s.splitlines()
print(res)

res = [s.upper() for s in res]
print(res)

print([len(s) for s in res])


print([s.count('A') for s in res])

s = " a , b , c , d"
res = s.split(',')
print(res)
res = [s.strip() for s in res]
print(res)

print(','.join(res))
print(','.join(['a']))

print(','.join(['a','b']))


print(type('a'))
print(type(b'a'))
print(b'a')


s = 'abcd'
print(s[0])

# s[0] = 'f'


b = b'abcd'
print(b[0])
# b[0] = 102

ba = bytearray(b)
print(ba)
ba[0] = 102

print(ba)





