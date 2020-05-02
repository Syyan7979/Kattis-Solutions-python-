def out(someList):
	counter = True
	for i in range(1, someList[-1]+1):
		if i not in someList:
			print(i)
			counter = False
	if counter:
		print("good job")

n = int(input())
out([int(input()) for i in range(n)])