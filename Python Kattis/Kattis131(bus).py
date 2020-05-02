def bus(n):
	if n == 1:
		return 1
	return 1 + 2 * bus(n-1)

n = int(input())
[print(bus(int(input()))) for i in range(n)]