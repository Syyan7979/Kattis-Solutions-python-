def odd(someList):
	for i in someList:
		if someList.count(i) == 1:
			return i
n = int(input())
for i in range(1, n+1):
	n = int(input())
	out = odd(input().split())
	print(f"Case #{i}: {out}")