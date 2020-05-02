import string
def decrypt(message, key):
	alphabet = string.ascii_uppercase
	out = ""
	for i in range(len(message)):
		ind1 = alphabet.index(key[i])
		ind2 = alphabet.index(message[i])
		if i % 2 != 0:
			out += alphabet[(ind1 + ind2)%26]
		else:
			if ind2 - ind1 < 0:
				out += alphabet[(26+ind2 - ind1)%26]
			else:
				out += alphabet[(ind2 - ind1)%26]
	print(out)
a = input()
b = input()
decrypt(a, b)