def erase(n, someList, comparison):
	even = someList
	odd = ""
	for i in someList:
		if i == "1":
			odd += "0"
		else:
			odd += "1"
	if n % 2 == 0:
		if comparison == even:
			print("Deletion succeeded")
		else:
			print("Deletion failed")
	else:
		if comparison == odd:
			print("Deletion succeeded")
		else:
			print("Deletion failed")
m, a, b = int(input()), input(), input()
erase(m, a, b)