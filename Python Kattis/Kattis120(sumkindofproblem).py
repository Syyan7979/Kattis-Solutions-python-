def sums(someList):
	nSum, eSum, oSum = 0, 0, 0
	for i in range(1, someList[1]+1):
		nSum += i
	for i in range(1, 2*someList[1]+1):
		if i % 2 == 0:
			eSum += i
		else:
			oSum += i
	print(someList[0], nSum, oSum, eSum)
n = int(input())
[sums([int(i) for i in input().split()]) for i in range(n)]