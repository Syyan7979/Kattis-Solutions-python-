def unique(someList):
	d = {}
	for i in someList:
		if i in d:
			d[i] += 1
		else:
			d[i] = 1
	return len(list(d.keys()))

N = int(input())
for i in range(N):
	M = int(input())
	out = [input() for i in range(M)]
	print(unique(out))