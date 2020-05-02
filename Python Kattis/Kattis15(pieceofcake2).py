def cake(N, H, V):
	out = 0
	if N-H > H:
		if N - V > V:
			out += 4 * (N-H) * (N-V)
		else:
			out += 4 * (N-H) * V
	else:
		if N - V > V:
			out += 4 * (H) * (N-V)
		else:
			out += 4 * (H) * V
	return out

n, h, v = [int(i) for i in input().split()]
print(cake(n, h, v))