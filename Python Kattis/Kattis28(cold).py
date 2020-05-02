def cold(N, someList):
	counter = 0
	for i in someList:
		if i < 0:
			counter += 1
	return counter

n = int(input())
lst = [int(i) for i in input().split()]

print(cold(n, lst))