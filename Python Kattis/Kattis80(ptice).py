Adrian, Bruno, Goran = "ABC", "BABC", "CCAABB"
def comparison(string):
	a, b, c = ["Adrian", 0], ["Bruno", 0], ["Goran", 0]
	for i in range(n):
		if string[i] == Adrian[i%3]:
			a[1] += 1
		if string[i] == Bruno[i%4]:
			b[1] += 1
		if string[i] == Goran[i%6]:
			c[1] += 1
	m = [a, b, c]
	print(max(a[1], b[1], c[1]))
	for i in m:
		if i[1] == max(a[1], b[1], c[1]):
			print(i[0])
n = int(input())
comparison(input())