def days(someList):
	bigList = []
	for i in someList:
		for j in range(i[0], i[1]+1):
			if j not in bigList:
				bigList.append(j)
	print(len(bigList))
n = int(input())
days([[int(i) for i in input().split()] for x in range(n)])