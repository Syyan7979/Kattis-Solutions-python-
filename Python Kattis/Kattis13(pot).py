def power(someString):
	out = int(someString[:-1]) ** int(someString[-1])
	return out

N = int(input())
outList = [power(input()) for i in range(N)]
print(sum(outList))