def factorial(someInt):
	if someInt == 0:
		return 1
	return someInt * factorial(someInt-1)

N = int(input())
outList = [print(str(factorial(int(input())))[-1]) for i in range(N)]