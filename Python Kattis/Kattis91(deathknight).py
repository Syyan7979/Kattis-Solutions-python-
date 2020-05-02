def dumb(someList):
	out = 0
	for i in someList:
		if "CD" not in i:
			out += 1
	print(out)
n = int(input())
dumb([input() for i in range(n)])