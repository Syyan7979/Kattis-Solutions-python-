def bijele(someList):
	comparison = [1, 1, 2, 2, 2, 8]
	out = ""
	for i in range(6):
		out += f"{comparison[i] - someList[i]} "
	return out
print(bijele([int(i) for i in input().split()]))