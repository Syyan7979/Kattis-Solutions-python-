from math import floor
def gerry(someList):
	V = 0
	tWa = 0
	tWb = 0
	for i in someList:
		winner = ""
		wa = 0
		wb = 0
		if i[1] > i[2]:
			winner = "A"
			wb = i[2]
			wa = i[1] - (floor((i[1] + i[2])/2) + 1)
		else:
			winner = "B"
			wa = i[1]
			wb = i[2] - (floor((i[1] + i[2])/2) + 1)
		tWa += wa
		tWb += wb
		V += i[1] + i[2]
		print(winner, wa, wb)
	print(abs(tWa-tWb)/V)

P, D = [int(i) for i in input().split()]
dic = {}
bigList = []
for i in range(P):
	d, a, b = [int(i) for i in input().split()]
	if d in dic:
		dic[d][0], dic[d][1] = dic[d][0] + a, dic[d][1] + b
	else:
		dic[d] = [a,b]
for k,v in dic.items():
	bigList.append([k] + v)
bigList.sort()
gerry(bigList)