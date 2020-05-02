def ez(a, b, c):
	if b-a > c-b:
		print(b-a-1)
	else:
		print(c-b-1)
A, B, C = [int(i) for i in input().split()]
ez(A, B, C)