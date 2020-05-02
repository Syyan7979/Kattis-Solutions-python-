def trik(string):
	cups = ["A", "B", "C"]
	for i in string:
		if i == "A":
			cups[0], cups[1] = cups[1], cups[0]
		elif i == "B":
			cups[1], cups[2] = cups[2], cups[1]
		elif i == "C":
			cups[0], cups[2] = cups[2], cups[0]
	if string[0] == "A" or string[0] == "C":
		return cups.index("A") + 1
	else:
		return cups.index("B") + 1
someString = input()
print(trik(someString))