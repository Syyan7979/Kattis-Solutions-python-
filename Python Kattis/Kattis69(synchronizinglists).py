def comparison(lst1, lst2, someInt):
	m1 = sorted(lst1)
	m2 = sorted(lst2)
	for i in range(n):
		hi = m1.index(lst1[i])
		print(m2[hi])
	print()
while True:
	n = int(input())
	if n == 0:
		break
	else:
		l1 = [int(input()) for i in range(n)]
		l2 = [int(input()) for i in range(n)]
		comparison(l1, l2, n)