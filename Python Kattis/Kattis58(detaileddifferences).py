def difference(someList, someInt):
	for i in range(0, 2*someInt, 2):
		out = ""
		for j in range(len(someList[i])):
			if someList[i][j] == someList[i+1][j]:
				out += "."
			else:
				out += "*"
		print(someList[i])
		print(someList[i+1])
		print(out)
		print()

n = int(input())
ans = difference([input() for i in range(2*n)], n)