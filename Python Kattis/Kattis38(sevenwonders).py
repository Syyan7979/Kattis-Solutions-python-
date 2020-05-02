def seven(string):
	T = string.count("T")
	C = string.count("C")
	G = string.count("G")
	current = T**2 + C**2 + G**2
	counter = 0
	while T != 0 and C != 0 and G != 0:
		T -= 1
		C -= 1
		G -= 1
		counter += 1
	current += counter * 7
	return current
print(seven(input()))