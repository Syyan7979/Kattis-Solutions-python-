def combination(a,b):
	if a[-2:] == "ex":
		return a+b
	else:
		if a[-1] == "e":
			return a+"x"+b
		elif a[-1] in "aiou":
			return a[:-1]+"ex"+b
		else:
			return a + "ex" + b
Y, P = input().split()
print(combination(Y, P))