def repeats(someInt):
	return len(set(str(someInt))) == len(str(someInt))
def divisible(someInt):
	out = True
	for i in str(someInt):
		if someInt % int(i) != 0:
			out = False
			break
	return out
def combi(s, e):
	count = 0
	for i in range(s, e+1):
		if repeats(i) and "0" not in str(i) and divisible(i):
			count += 1
	print(count)
a, b = [int(i) for i in input().split()]
combi(a, b)