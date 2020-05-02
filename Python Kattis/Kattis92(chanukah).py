def chanukah(n, someInt):
	out = 0
	for i in range(1, someInt+1):
		out += i
	print(f"{n} {out+ someInt}")

n = int(input())
for i in range(n):
	N, D = [int(i) for i in input().split()]
	chanukah(N, D)