def smallest(someList):
	return someList.index(min(someList))

n = int(input())
print(smallest([int(i) for i in input().split()]))