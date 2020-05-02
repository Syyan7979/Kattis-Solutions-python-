def group(someList):
	out = 0
	for i in range(n):
		out += someList[i] * (4/5)**i
	print(out/5)
def average(someList):
	final = 0
	for i in range(n):
		out = 0
		givenList = someList[:i] + someList[i+1:]
		for j in range(n-1):
			out += givenList[j] * (4/5)**j
		final += out/5
	print(final/n)
n= int(input())
ans = [int(input()) for i in range(n)]
group((ans))
average(ans)