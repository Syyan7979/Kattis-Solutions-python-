def repeats(string):
	out = "-"
	for i in range(len(string)):
		if string[i] != out[-1]:
			out += string[i]
	print(out[1:])
repeats(input())