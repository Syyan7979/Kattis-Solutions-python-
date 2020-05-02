def conversion(someInt, base):
	out = (someInt%base)**2
	if someInt == 0:
		return out
	return out + conversion(someInt//base, base)
N = int(input())
for i in range(N):
	K, b, n = [int(i) for i in input().split()]
	print(f"{K} {conversion(n, b)}")