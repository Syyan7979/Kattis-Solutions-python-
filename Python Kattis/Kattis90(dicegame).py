"""def out(a, b, c, d):
	dic = {}
	for i in range(a, b+1):
		for j in range(c, d+1):
			if i + j in dic:
				dic[i + j] += 1
			else:
				dic[i + j] = 1
	for i in dic.keys():
		dic[i] = dic[i] / ((b-a+1) * (d-c+1))
	return dic
A1, B1, C1, D1 = [int(i) for i in input().split()]
A2, B2, C2, D2 = [int(i) for i in input().split()]
Gunrar = out(A1, B1, C1, D1)
emma = out(A2, B2, C2, D2)

print(Gunrar)
print(emma)
if Gunrar > emma:
	print("Gunrar")
elif emma > Gunrar:
	print("Emma")
else:
	print("Tie")"""

A1, B1, C1, D1 = [int(i) for i in input().split()]
A2, B2, C2, D2 = [int(i) for i in input().split()]

def prob(a, b, c, d):
	amin = a + c
	amax = b + d
	return amin, amax

gunrarMin, gunrarMax = prob(A1, B1, C1, D1)
emmaMin, emmaMax = prob(A2, B2, C2, D2)
idk = max(gunrarMin, emmaMin) - min(gunrarMin, emmaMin)
idk2 = max(gunrarMax, emmaMax) - min(gunrarMax, emmaMax)

if gunrarMin > emmaMax:
	print("Gunrar")
elif emmaMin > gunrarMax:
	print("Emma")
else:
	if idk == idk2:
		print("Tie")
	elif idk2 > idk:
		if max(gunrarMax, emmaMax) == gunrarMax:
			print("Gunrar")
		else:
			print("Emma")
	else:
		if min(gunrarMin, emmaMin) == gunrarMin:
			print("Emma")
		else:
			print("Gunrar")

