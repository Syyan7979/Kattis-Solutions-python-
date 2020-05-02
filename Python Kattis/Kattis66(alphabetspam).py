import string
def spam(some):
	wC = some.count("_")
	lC = 0
	uC = 0
	sC = 0
	for i in some:
		if i in string.ascii_lowercase:
			lC += 1
		if i in string.ascii_uppercase:
			uC += 1
		if i not in string.ascii_uppercase + string.ascii_lowercase + "_":
			sC += 1
	print(wC/len(some))
	print(lC/len(some))
	print(uC/len(some))
	print(sC/len(some))
spam(input())