def star(someInt):
	print(f"{someInt}:")
	for i in range(2, someInt):
		for j in range(i-1, i+1):
			curSum = i
			while True: 
				curSum += j
				if curSum == someInt:
					print(f"{i},{j}")
					break
				else:
					curSum += i
					if curSum == someInt:
						print(f"{i},{j}")
						break
					elif curSum > someInt:
						break
n = int(input())
star(n)