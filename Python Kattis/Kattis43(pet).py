def fuck(someList):
	listMax = max(someList)
	return f"{someList.index(listMax) + 1} {listMax}"

lst = [sum([int(i) for i in input().split()]) for i in range(5)]
print(fuck(lst))