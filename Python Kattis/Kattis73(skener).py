def scan(someList, zR, zC):
	for i in someList:
		out = ""
		for j in i:
			out += zC * j
		for i in range(zR):
			print(out)

r, c, Zr, Zc = [int(i) for i in input().split()]
out = scan([input() for i in range(r)], Zr, Zc)