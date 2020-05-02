def v(someList):
	for i in someList:
		if someList.count(i) == 1:
			return i
			break
lst1 = []
lst2 = []
for i in range(3):
	x, y = [int(i) for i in input().split()]
	lst1.append(x)
	lst2.append(y)

print(v(lst1), v(lst2))