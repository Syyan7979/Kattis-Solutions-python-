def counter(someList, someInt):
	accum = 0
	curr = 0
	for i in range(someInt):
		accum += someList[i][0] * (someList[i][1] - curr)
		curr = someList[i][1]
	return accum

while True:
	n = int(input())
	if n == -1:
		break
	else:
		lst = [[int(i) for i in input().split()] for i in range(n)]
		print(f"{counter(lst, n)} miles")