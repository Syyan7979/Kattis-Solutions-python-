import random
a, b = [int(i) for i in input().split()]
l = [i for i in range(1, a+1)]
m = [l.remove(int(input())) for i in range(b)]
if len(l) == 0:
	print("too late")
else:
	print(random.choice(l))