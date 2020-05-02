def min(L, D, X):
	for N in range(L, D+1):
		nList = [int(i) for i in str(N)]
		if sum(nList) == X:
			return N
			break

def max(L, D, X):
	for M in range(D, L-1, -1):
		mList = [int(i) for i in str(M)]
		if sum(mList) == X:
			return M
			break

L = int(input())
D = int(input())
X = int(input())

print(min(L, D, X))
print(max(L, D, X))