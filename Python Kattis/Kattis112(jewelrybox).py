def optimization(X, Y):
	A = 12
	B = -2*((X*2)+(Y*2))
	C = X*Y
	x1 = (-B + ((B**2 - (4*A*C))**(1/2)))/ (2*A)
	x2 = (-B - ((B**2 - (4*A*C))**(1/2)))/ (2*A)
	if x1 < x2 or x1 == x2:
		print((X - (2*x1)) * (Y - (2*x1)) * x1)
	else:
		print((X - (2*x2)) * (Y - (2*x2)) * x2)
n = int(input())
for i in range(n):
	a, b = [int(i) for i in input().split()]
	optimization(a, b)