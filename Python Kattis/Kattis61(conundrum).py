def chris(string):
	counter = 0
	comparison = 0
	per = "PER"
	for i in range(len(string)):
		if string[i] == per[comparison]:
			if comparison == 2:
				comparison = 0
			else:
				comparison += 1
		else:
			if comparison == 2:
				counter += 1
				comparison = 0
			else:
				counter += 1
				comparison += 1
	print(counter)
chris(input().upper())