def transitwoes(first, second, third, fourth):
	travelTime = first[1] - first[0]
	currentTime = 0
	busTime = 0
	for i in range(first[2]):
		busTime += fourth[i]
		currentTime += second[i]
		if busTime > currentTime:
			currentTime = busTime
		currentTime += third[i]
	return currentTime + second[first[2]] <= travelTime

lst1 = [int(i) for i in input().split()]
lst2 = [int(i) for i in input().split()]
lst3 = [int(i) for i in input().split()]
lst4 = [int(i) for i in input().split()]

if transitwoes(lst1, lst2, lst3, lst4):
	print("yes")
else:
	print("no")