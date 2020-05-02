def matrix(someList, n):
	d = {}
	out = ""
	for i in range(n):
		d[i] = False

	for i in range(n):
		if d[i] == True:
			pass
		else:
			for j in range(n):
				if someList[i][j] == 1:
					if checker(someList, j, n, i) != -1:
						d[i], d[j], d[checker(someList, j, n, i)] = True, True, True
						break
	for i in range(n):
		if list(d.values())[i] == False:
			out += f"{i} "
	print(out)

def checker(someList, pos, m, comparison):
	for i in range(pos, m):
		if someList[pos][i] == 1:
			if someList[i][comparison] == 1:
				return i
				break
	return -1
while True:
	n = int(input())
	if n == -1:
		break
	else:
		matrix([[int(i) for i in input().split()] for x in range(n)], n)