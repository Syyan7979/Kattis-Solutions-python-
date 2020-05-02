def soda(A, b):
	if A < b:
		return 0
	return soda(A//b + A%b, b) + A // b
E, F, C = [int(i) for i in input().split()]
print(soda(E+F, C))