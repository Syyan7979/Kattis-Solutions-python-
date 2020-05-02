import string
def pangram(someString):
	alphabet = string.ascii_lowercase
	out = ""
	for i in range(26):
		if alphabet[i] not in someString:
			out += alphabet[i]
	if out == "":
		print("pangram")
	else:
		print(f"missing {out}")
n = int(input())
ans = [pangram(input().lower()) for i in range(n)]