def gcd(a, b):
	if a % b == 0:
		return b
	return gcd(b, a%b)

def circles(someList):
	multiplier = [1, 1]
	for i in range(1, n):
		if (someList[i-1] * multiplier[0]) % (someList[i] * multiplier[1]) == 0:
			print(f"{(someList[i-1] * multiplier[0]) // (someList[i] * multiplier[1])}/1")
			multiplier = [(someList[i-1] * multiplier[0]) // (someList[i] * multiplier[1]), 1]
		else:
			divisor = gcd((someList[i-1] * multiplier[0]), (someList[i] * multiplier[1]))
			if divisor != 1:
				num = someList[i-1] * multiplier[0]
				denom = someList[i] * multiplier[1]
				while num % divisor == 0 and denom % divisor == 0:
					num = num // divisor
					denom = denom // divisor
				print(f"{num}/{denom}")
				multiplier = [num, denom]
			else:
				print(f"{someList[i-1] * multiplier[0]}/{someList[i] * multiplier[1]}")
				multiplier = [someList[i-1] * multiplier[0], someList[i] * multiplier[1]]
n = int(input())
circles([int(i) for i in input().split()])