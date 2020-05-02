def indivArea(someList):
	return someList[0] * someList[1]
n = int(input())
pieces = int(input())
print(sum([indivArea( [int(i) for i in input().split()]) for i in range(pieces)]) // n)