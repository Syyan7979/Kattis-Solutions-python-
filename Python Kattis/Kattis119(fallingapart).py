def separation(someList):
	Alice, Bob = 0, 0
	for i in range(n):
		if i % 2 == 0:
			Alice += someList[i]
		else:
			Bob += someList[i]
	print(Alice, Bob)

n = int(input())
out = [int(i) for i in input().split()]
out.sort(reverse = True)
separation(out)