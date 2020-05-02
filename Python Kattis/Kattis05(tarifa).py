def tarifa(X, nList):
	currentBal = 0
	for i in nList:
		currentBal += X
		currentBal -= i
	return currentBal + X
	
X = int(input())
N = int(input())
someList = [int(input()) for i in range(N)]
print(tarifa(X, someList))