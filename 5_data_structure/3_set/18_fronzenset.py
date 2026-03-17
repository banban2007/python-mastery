fs=frozenset([1,2,3,4,5,6,7,8])
print(type(fs))
for i in fs:
	print(i)
fs.remove(7)#AttributeError: 'frozenset' object has no attribute 'remove'
print(fs)
fs.add(9)#AttributeError: 'frozenset' object has no attribute 'add'