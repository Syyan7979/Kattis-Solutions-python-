def dumb(someString):
	return len(someString)
n = int(input())
out = [print(dumb(input())) for i in range(n)]