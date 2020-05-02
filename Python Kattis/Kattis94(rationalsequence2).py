def rationalSequence(p, q):
	out = []
	while p != 1 or q != 1:
		if p/q > 1:
			p -= q
			out.append(0)
		else:
			q -= p
			out.append(1)
	start = 2 ** len(out)
	end = 2 * start - 1
	for i in out[::-1]:
		center = (start + end) // 2
		if i == 1:
			end = center
		else:
			start = center
	return end

n = int(input())
for i in range(n):
	N, M = input().split()
	P, Q = [int(i) for i in M.split("/")]
	print(N, rationalSequence(P, Q))