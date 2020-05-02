vowels = list("aeiou")
def decode(someList):
	out = ""
	for i in someList:
		j = 0
		word = ""
		while j < len(i):
			if i[j] in vowels:
				word += i[j]
				j += 3
			else:
				word += i[j]
				j += 1
		out += f"{word} "
	return out
print(decode(input().split()))