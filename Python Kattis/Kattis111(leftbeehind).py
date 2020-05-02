def stupido(A, B):
	if A+B == 13:
		print("Never speak again.")
	else:
		if A > B:
			print("To the convention.")
		elif A < B:
			print("Left beehind.")
		else:
			print("Undecided.")
while True:
	a, b = [int(i) for i in input().split()]
	if a == 0 and b == 0:
		break
	else:
		stupido(a, b)