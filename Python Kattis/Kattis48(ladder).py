from math import pi, sin, ceil
def soh(o, deg):
	rad = (deg * pi) / 180
	H = o / (sin(rad))
	return ceil(H)

h, v = [int(i) for i in input().split()]
print(soh(h, v))