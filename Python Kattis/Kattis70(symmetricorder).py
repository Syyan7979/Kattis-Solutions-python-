def ordering(someList):
	if n % 2 == 0:
		for i in range(0, n, 2):
			print(someList[i])
		for i in range(n-1, 0, -2):
			print(someList[i])
	else:
		for i in range(0, n, 2):
			print(someList[i])
		for i in range(n-2, 0, -2):
			print(someList[i])
wassap = 1
while True:
	n = int(input())
	if n == 0:
		break
	else:
		print(f"SET {wassap}")
		out = ordering([input() for i in range(n)])
		wassap +=1