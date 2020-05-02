def qaly(someList):
	out = 0
	for i in range(N):
		out += someList[i][0] * someList[i][1]
	return out

N = int(input())
lst = [[float(i) for i in input().split()] for j in range(N)]
print(qaly(lst))