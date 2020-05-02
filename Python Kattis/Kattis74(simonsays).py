def simonSays(someList):
	for i in someList:
		if "Simon says" in i:
			print(i[10:])
n = int(input())
simonSays([input() for i in range(n)])