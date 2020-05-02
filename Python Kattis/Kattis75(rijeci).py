def rijeci(someInt):
	if someInt == 0:
		return "A"
	elif someInt == 1:
		return "B"
	return rijeci(someInt-1) + rijeci(someInt-2)
out = rijeci(int(input()))
print(out.count("A"), out.count("B"))

"""
n = int(input())

A = 1
B = 0
for i in range(n):
    A, B = B, A + B

print(f"{A} {B}")"""