def text(someString):
	basis = []
	a = len(someString)
	for i in range(a//3, a+1, a//3):
		basis.append(someString[i-(a//3):i])
	return basis
def ans(someList):
	for i in someList:
		if someList.count(i) > 1:
			print(i)
			break
ans(text(input()))