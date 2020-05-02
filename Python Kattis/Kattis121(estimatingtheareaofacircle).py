from math import pi
def estimate(R, M, C):
	correct = pi*(R**2)
	estimate = (2*R)**2 * (C/M)
	print(correct, estimate)
while True:
	r, m, c = [float(i) for i in input().split()]
	if r == 0 and m == 0 and c == 0:
		break
	else:
		estimate(r, m, c)