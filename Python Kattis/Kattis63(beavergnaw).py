from math import pi
def diameter(D, V):
	redVol = ((D/2)**2 * pi * D) - V
	sD = ((4 * redVol)/pi)**(1/3)
	print(sD)

while True:
	d, v = [int(i) for i in input().split()]
	if d == 0 and v == 0:
		break
	else:
		diameter(d, v)