def lineUp(someList):
	pos = [1]*n
	currentNum = 2
	for i in someList:
		pos[1 + i] = currentNum
		currentNum += 1
	for i in pos:
		print(i, end = " ")
n = int(input())
lineUp([int(i) for i in input().split()])