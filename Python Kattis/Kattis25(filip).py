def flip(a, b):
	if int(a[::-1]) > int(b[::-1]):
		return a[::-1]
	else:
		return b[::-1]

A, B = input().split()
print(flip(A, B))