def spavanac(h, m):
	if h == 0:
		minutes = (24 * 60 + m) - 45
		nH = minutes//60
		nM = minutes%60
		print(nH, nM)
	else:
		minutes = (h * 60 + m) - 45
		nH = minutes//60
		nM = minutes%60
		print(nH, nM)

H, M = [int(i) for i in input().split()]
spavanac(H, M)