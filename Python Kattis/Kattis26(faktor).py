from math import ceil
def factor(a, b):
	for i in range(a*b, 0, -1):
		if ceil(i/a) < b:
			return i + 1
			break

A, B = [int(i) for i in input().split()]
print(factor(A, B))