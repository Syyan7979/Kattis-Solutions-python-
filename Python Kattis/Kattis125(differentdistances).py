def manhattan(a, b, c, d, p):
	out = ((abs(a-c))**p + (abs(b-d))**p)**(1/p)
	print(out)

while True:
	a = input()
	if a == "0":
		break
	else:
		x1, y1, x2, y2, p = [float(i) for i in a.split()]
		manhattan(x1, y1, x2, y2, p)