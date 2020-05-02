def odd(someInt):
	if someInt % 2 == 0:
		return f"{someInt} is even"
	else:
		return f"{someInt} is odd"
N = int(input())
someList = [print(odd(int(input()))) for i in range(N)]