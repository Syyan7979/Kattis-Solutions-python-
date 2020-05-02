def easiest(someString):
	comaparison = 0
	for i in someString:
		comaparison += int(i)
	counter = 11
	while True:
		against = 0
		for i in str(int(someString) * counter):
			against += int(i)
		if against == comaparison:
			break
		else:
			counter += 1
	print(counter)
while True:
	n = input()
	if n == "0":
		break
	else:
		easiest(n)