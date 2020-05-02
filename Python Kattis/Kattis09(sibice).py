from math import sqrt
def sibice(someInt):
	if someInt <= W or someInt <= H or someInt <= D:
		print("DA")
	else:
		print("NE")

N, W, H = [int(i) for i in input().split()]
D = sqrt(W**2 + H**2)
out = [sibice(int((input()))) for i in range(N)]