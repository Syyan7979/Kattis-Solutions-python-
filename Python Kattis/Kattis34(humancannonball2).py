from math import cos, sin, pi
def cannon(v, d, x, h1, h2):
	deg = (d * pi)/180
	t = x / (v * cos(deg))
	y = (v * t * sin(deg)) - (0.5 * 9.81 * (t**2))
	if h1 + 1 < y < h2 - 1:
		return "Safe"
	else:
		return "Not Safe"
n = int(input())
for i in range(n):
	V, D, X, H1, H2 = [float(i) for i in input().split()]
	print(cannon(V, D, X, H1, H2))