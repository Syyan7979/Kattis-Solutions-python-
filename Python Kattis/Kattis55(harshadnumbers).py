def harshad(someString):
	while True:
		numSum = 0
		for i in someString:
			numSum += int(i)
		if int(someString) % numSum == 0:
			return someString
			break
		else:
			someString = str(int(someString)+1)
print(harshad(input()))