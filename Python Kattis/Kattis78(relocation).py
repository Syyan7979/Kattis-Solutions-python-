def relocation(a, b, c):
	if a == 1:
		ans[b-1] = c
	elif a == 2:
		if ans[b-1] > ans[c-1]:
			print(ans[b-1]-ans[c-1])
		else:
			print(ans[c-1]-ans[b-1])

N, Q = [int(i) for i in input().split()]
ans = [int(i) for i in input().split()]
for i in range(Q):
	A, B, C = [int(i) for i in input().split()]
	relocation(A, B, C)