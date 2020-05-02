import string
alphabet = string.ascii_uppercase
def message(someString):
	counter = 0
	out = ""
	for i in someString:
		counter += alphabet.index(i)
	for i in someString:
		out += alphabet[(alphabet.index(i) + counter)%26]
	return out
def conversion(A, B):
	out = ""
	for i in range(len(A)):
		out += alphabet[(alphabet.index(A[i]) + alphabet.index(B[i])) % 26]
	print(out)
	
ab = input()
a, b = ab[:len(ab)//2], ab[len(ab)//2:]
w1, w2 = message(a), message(b)
conversion(w1, w2)