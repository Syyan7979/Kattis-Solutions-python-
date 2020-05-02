def nasty(R, E, C):
	if E - C > R:
		print("advertise")
	elif E - C < R:
		print("do not advertise")
	else:
		print("does not matter")

N = int(input())
for i in range(N):
	r, e, c = [int(i) for i in input().split()]
	nasty(r, e, c)