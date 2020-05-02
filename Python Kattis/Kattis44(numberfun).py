def fun(a, b, c):
	if a + b == c or a - b == c or b - a == c or a * b == c or (a // b == c and a % b == 0) or (b // a == c and b % a == 0):
		return "Possible"
	else:
		return "Impossible"

n = int(input())
for i in range(n):
	A, B, C = [int(i) for i in input().split()]
	print(fun(A, B, C))