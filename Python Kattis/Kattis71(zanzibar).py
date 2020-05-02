def zanzi(someList):
	count = 0
	for i in range(1, len(someList)):
		if someList[i] > 2 * someList[i-1]:
			count += someList[i] - 2 * someList[i-1]
	print(count)
n = int(input())
for i in range(n):
	out = zanzi([int(i) for i in input().split()])