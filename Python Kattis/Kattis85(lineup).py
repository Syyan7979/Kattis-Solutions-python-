def lineUp(someList):
	sort = sorted(someList)
	sortRev = sorted(someList, reverse = True)
	if someList == sort:
		print("INCREASING")
	elif someList == sortRev:
		print("DECREASING")
	else:
		print("NEITHER")
n = int(input())
lineUp([input() for i in range(n)])