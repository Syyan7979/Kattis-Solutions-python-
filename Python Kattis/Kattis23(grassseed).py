def price(someList):
	return p * someList[0] * someList[1]

p = float(input())
l = int(input())
outList = [price([float(i) for i in input().split()]) for i in range(l)]
print(sum(outList))