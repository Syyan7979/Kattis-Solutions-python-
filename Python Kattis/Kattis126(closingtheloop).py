from collections import deque
def closing(m, someList):
	B = []
	R = []
	for i in range(m):
		if someList[i][-1] == "R":
			R.append(int(someList[i][:-1]))
		else:
			B.append(int(someList[i][:-1]))
	B.sort(reverse = True)
	R.sort(reverse = True)
	return deque(B), deque(R)
def outcome(a, b):
	out = 0
	while len(a) != 0 and len(b) != 0:
		out += a[0] + b[0] - 2
		a.popleft()
		b.popleft()
	return out

r = int(input())
for i in range(1, r+1):
	n = int(input())
	hello = input().split()
	if n == 1:
		print(f"Case #{i}: {0}")
	else:
		b, r = closing(n, hello)
		print(f"Case #{i}: {outcome(b, r)}")