def inside(someList):
	currentMax = 0
	entrance, entrance2 = 0, 0
	for i in range(R-K+1):
		for j in range(S-K+1):
			counter = 0
			for k in range(i+1, i+K - 1):
				for l in range(j + 1, j+K-1):
					if someList[k][l] == "*":
						counter += 1
			if counter > currentMax:
				currentMax = counter
				entrance, entrance2 = i, j
	for i in range(entrance, entrance+K):
		for j in range(entrance2, entrance2+K):
			if (i == entrance and j == entrance2) or (i == entrance+K-1 and j == entrance2) or (i == entrance and j == entrance2+K-1) or (i == entrance+K-1 and j == entrance2+K-1):
				someList[i] = someList[i][:j] + "+" + someList[i][j+1:]
			elif i == entrance or i == entrance+K-1:
				someList[i] = someList[i][:j] + "-" + someList[i][j+1:]
			elif j == entrance2 or j == entrance2+K-1:
				someList[i] = someList[i][:j] + "|" + someList[i][j+1:]
	return currentMax, someList
R, S, K = [int(i) for i in input().split()]
bigList = [input() for i in range(R)]
a,b = inside(bigList)
print(a)
out = [print(i) for i in b]