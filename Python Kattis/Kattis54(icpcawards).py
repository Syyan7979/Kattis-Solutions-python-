def winners(someList):
	comparison = []
	for i in someList:
		if i[0] in comparison:
			pass
		elif len(comparison) == 12:
			break
		else:
			comparison.append(i[0])
			print(i[0], i[1])
n = int(input())
out = winners([input().split() for i in range(n)])