def arrange(someList):
	while someList != [1, 2, 3, 4, 5]:
		for i in range(1, 5):
			if someList[i-1] > someList[i]:
				someList[i-1], someList[i] = someList[i], someList[i-1]
				print(str(someList)[1:-1].replace(",", ""))
arrange([int(i) for i in input().split()])