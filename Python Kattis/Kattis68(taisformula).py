def tai(someList, m):
	out = 0
	for i in range(m-1):
		out += (someList[i][1] + someList[i+1][1])/2 * (someList[i+1][0]-someList[i][0])
	print(out/1000)

n = int(input())
hi = tai([[float(i) for i in input().split()] for i in range(n)], n)