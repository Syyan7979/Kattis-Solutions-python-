import string
def stack(someList):
	someList.sort(key = lambda x: x[1])
	for i in someList:
		print(i[0])

n = int(input())
bigList = []
for i in range(n):
	x, y = input().split()
	if x[0] in string.ascii_lowercase:
		bigList.append([x, int(y)])
	else:
		bigList.append([y, int(x)/2])
stack(bigList)