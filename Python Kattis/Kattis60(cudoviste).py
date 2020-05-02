def cudoviste(someList, r, c):
	d = {0:0, 1:0, 2:0, 3:0, 4:0}
	for i in range(r-1):
		for j in range(c-1):
			lst = [someList[i][j], someList[i][j+1], someList[i+1][j], someList[i+1][j+1]]
			if lst.count(".") == 4:
				d[0] += 1
			elif lst.count("X") == 1 and lst.count("#") == 0:
				d[1] += 1
			elif lst.count("X") == 2 and lst.count("#") == 0:
				d[2] += 1
			elif lst.count("X") == 3 and lst.count("#") == 0:
				d[3] += 1
			elif lst.count("X") == 4 and lst.count("#") == 0:
				d[4] += 1
	for i in d.values():
		print(i)
R, C = [int(i) for i in input().split()]
out = cudoviste([input() for i in range(R)], R, C)