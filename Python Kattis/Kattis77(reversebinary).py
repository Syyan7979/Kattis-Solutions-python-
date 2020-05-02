def binary(someInt):
	out = ""
	if someInt == 0:
		return out
	return binary(someInt//2) + str(someInt%2)

n = int(input())
reverse = binary(n)[::-1]
out = 0
counter = 0
for i in range(len(reverse)-1, -1, -1):
	out += int(reverse[counter]) * (2**i)
	counter += 1
print(out)