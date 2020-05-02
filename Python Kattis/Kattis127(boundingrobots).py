def robot(w, l, someList):
	x, y = 0, 0
	aX, aY = 0, 0
	for item in someList:
		if item[0] == "u":
			y += int(item[1])
			if aY + int(item[1]) > l - 1:
				aY = (l-1)
			else:
				aY += int(item[1])
		elif item[0] == "d":
			y -= int(item[1])
			if aY - int(item[1]) < 0:
				aY = 0
			else:
				aY -= int(item[1])
		elif item[0] == "r":
			x += int(item[1])
			if aX + int(item[1]) > w - 1:
				aX = (w-1)
			else:
				aX += int(item[1])
		elif item[0] == "l":
			x -= int(item[1])
			if aX - int(item[1]) < 0:
				aX = 0
			else:
				aX -= int(item[1])
	print(f"Robot thinks {x} {y}")
	print(f"Actually at {aX} {aY}")

while True:
	W, L = [int(i) for i in input().split()]
	if W == L == 0:
		break
	else:
		n = int(input())
		l = [input().split() for i in range(n)]
		robot(W, L, l)