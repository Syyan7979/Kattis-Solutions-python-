import sys
morse = {"A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....",
		 "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.",
		 "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
		 "Y": "-.--", "Z": "--..", "_": "..--", ",": ".-.-", ".": "---.", "?": "----"}
hello = []
revMorse = {}
for k, v in morse.items():
	hello.append((k, v))
for i in hello:
	revMorse[i[1]] = i[0]
def conversion(string):
	out = ""
	counter = ""
	for i in string:
		out += morse[i]
		counter += str(len(morse[i]))
	return out, counter[::-1]
def decode(string, counter):
	out = ""
	start = 0
	for i in range(0, len(counter)):
		out += revMorse[string[start:int(counter[i]) + start]]
		start += int(counter[i])
	print(out)
	
for lines in sys.stdin.readlines():
	a, b = conversion(lines)
	decode(a, b)