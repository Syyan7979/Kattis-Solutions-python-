def planina(N):
	if N == 0:
		return 2
	return 2**(N-1) + planina(N-1)
print(planina(int(input())) ** 2)