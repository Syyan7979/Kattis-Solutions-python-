def hydra(H, T, N):
	if H == 0 and T == 0:
		return N
	elif H == 1 and T == 0:
		return -1
	elif H != 0:
		if H == 1:
			if T % 2 == 0:
				return hydra(H+1, T-2, N+1)
			else:
				return hydra(H, T+1, N+1)
		else:
			return hydra(H-2, T, N+1)
	elif H == 0:
		if T % 2 == 0:
			if T == 2:
				return hydra(H, T+1, N+1)
			else:
				return hydra(H+1, T-2, N+1)
		else:
			return hydra(H, T+1, N+1)
while True:
	a, b = [int(i) for i in input().split()]
	if a == 0 and b == 0:
		break
	else:
		print(hydra(a, b, 0))