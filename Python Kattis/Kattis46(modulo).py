def mod(someList):
	d = {}
	for i in someList:
		if i % 42 in d:
			d[i % 42] += 1
		else:
			d[i % 42] = 1
	return len(list(d.keys()))

lst = [int(input()) for i in range(10)]
print(mod(lst))