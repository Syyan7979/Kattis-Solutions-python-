def scoring(someList):
	wrong = []
	score = 0
	correct = 0
	for i in someList:
		if i[2] == "right":
			score += int(i[0]) + (20 * wrong.count(i[1]))
			correct += 1
		else:
			wrong.append(i[1])
	print(correct, score)
bigList = []
while True:
	n = input().split()
	if n == ["-1"]:
		break
	else:
		bigList.append(n)
scoring(bigList)