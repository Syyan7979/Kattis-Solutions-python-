def single(someInt):
	return sum([int(i) for i in str(someInt)])
def checkSum(someList):
	for i in range(1, len(someList), 2):
		if someList[i] * 2 > 9:
			someList[i] = single(someList[i]*2)
		else:
			someList[i] *= 2
	return sum(someList) % 10 == 0
n = int(input())
for i in range(n):
	if checkSum([int(i) for i in input()[::-1]]):
		print("PASS")
	else:
		print("FAIL")