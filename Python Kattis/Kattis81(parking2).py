def parking(i):
	print((max(i) - min(i))*2)
n = int(input())
for i in range(n):
	m = int(input())
	parking([int(i) for i in input().split()])