def kingPos(someList):
	for i in range(2, someList[0]):
		if someList[i] - someList[i-1] != 1:
			print(i)
			break
n = int(input())
out = [kingPos([int(i) for i in input().split()]) for i in range(n)]