def batterup(someList):
	listSum = 0
	walks = 0
	for i in range(N):
		if someList[i] < 0:
			walks += 1
		else:
			listSum += someList[i]
	return listSum/(N-walks)

N = int(input())
print(batterup([int(i) for i in input().split()]))