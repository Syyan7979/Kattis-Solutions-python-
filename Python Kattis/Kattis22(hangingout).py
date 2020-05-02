def hangingOut(someList):
	stack = 0
	notAllowed = 0
	for i in range(x):
		if someList[i][0] == "enter":
			if stack + int(someList[i][1]) <= L:
				stack += int(someList[i][1])
			else:
				notAllowed += 1
		elif someList[i][0] == "leave":
			stack -= int(someList[i][1])
	return notAllowed
L, x = [int(i) for i in input().split()]
lst = [input().split() for i in range(x)]

print(hangingOut(lst))