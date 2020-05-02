def romans(val):
	out = round(val * 1000 * 5280 / 4854)
	return out
print(romans(float(input())))