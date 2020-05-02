from math import pi
import string
distance = 60*pi / 28
initialList = string.ascii_uppercase + " '"

def time(someString):
	out = 0
	for i in range(1, len(someString)):
		a = initialList.index(someString[i])
		b = initialList.index(someString[i-1])
		if a > b:
			if a - b < (28-a) + b:
				out += ((a - b) * distance) / 15
			else:
				out += (((28-a) + b) * distance) / 15
		else:
			if b - a < (28-b) + a:
				out += ((b - a) * distance) / 15
			else:
				out += (((28-b) + a) * distance) / 15
	print(out + len(someString))
n = int(input())
for i in range(n):
	time(input())