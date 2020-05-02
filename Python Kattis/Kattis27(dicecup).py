def dices(n, m):
	bigList = []
	outcomes = {}
	output = []
	for i in range(1, n+1):
		for j in range(1, m+1):
			hays = i + j
			if f"{hays}" in outcomes:
				outcomes[f"{hays}"] += 1
			else:
				outcomes[f"{hays}"] = 1

	largest = max(list(outcomes.values()))
	for k, v in outcomes.items():
		bigList.append((k, v))
	for x in range(len(bigList)):
		if bigList[x][1] == largest:
			output.append(int(bigList[x][0]))
	output.sort()
	return output

N, M = [int(i) for i in input().split()]
for i in dices(N,M):
	print(i)