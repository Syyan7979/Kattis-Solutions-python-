def r2(r1, s):
	R2 = 2*s - r1
	return R2

R1, S = [int(i) for i in input().split()]
print(r2(R1, S))