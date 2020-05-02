def mixedFractions(n, d):
	print(f"{n//d} {n%d} / {d}")

while True:
	N, D = [int(i) for i in input().split()]
	if N == 0 and D == 0:
		break
	else:
		mixedFractions(N, D)