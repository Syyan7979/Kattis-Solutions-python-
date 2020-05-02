def shades(someList):
	counter = 0
	pinkCounter = 0
	for i in someList:
		if "pink" in i:
			counter += 1
			pinkCounter += 1
		elif "rose" in i:
			counter += 1
	return counter, pinkCounter
n = int(input())
out, pink = shades([input().lower() for i in range(n)])

if pink == 0:
	print("I must watch Star Wars with my daughter")
else:
	print(out)