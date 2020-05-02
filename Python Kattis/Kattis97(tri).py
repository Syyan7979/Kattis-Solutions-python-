def tri(a, b, c):
	if a + b == c:
		print(f"{a}+{b}={c}")
	elif a == b + c:
		print(f"{a}={b}+{c}")
	elif a * b == c:
		print(f"{a}*{b}={c}")
	elif a == b * c:
		print(f"{a}={b}*{c}")
	elif a - b == c:
		print(f"{a}-{b}={c}")
	elif a == b - c:
		print(f"{a}={b}-{c}")
	elif a / b == c:
		print(f"{a}/{b}={c}")
	elif a == b / c:
		print(f"{a}={b}/{c}")
A, B, C = [int(i) for i in input().split()]
tri(A, B, C)