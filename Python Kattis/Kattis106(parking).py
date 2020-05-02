def answer(someList):
	a, b, c, d, e, f = someList
	fine = 0
	for i in range(min(someList)+1, max(someList)+1):
		if i in range(a+1, b+1) and i in range(c+1, d+1) and i in range(e+1, f+1):
			fine += 3*C
		elif (i in range(a+1, b+1) and i in range(c+1, d+1)) or (i in range(e+1, f+1) and i in range(c+1, d+1)) or (i in range(a+1, b+1) and i in range(e+1, f+1)):
			fine += 2*B
		elif i in range(a+1, b+1) or i in range(c+1, d+1) or i in range(e+1, f+1):
			fine += A
	print(fine)
A, B, C = [int(i) for i in input().split()]
basis = []
for i in range(3):
	basis += [int(i) for i in input().split()]
answer(basis)