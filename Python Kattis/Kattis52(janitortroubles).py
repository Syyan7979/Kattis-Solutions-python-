from math import sqrt
def maxArea(a, b, c, d):
	s = (a+b+c+d)/2
	return sqrt((s-a)*(s-b)*(s-c)*(s-d))
A, B, C, D = [int(i) for i in input().split()]
print(maxArea(A, B, C, D))