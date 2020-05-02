dominant = [11, 4, 3, 20, 10, 14, 0, 0]
notDominant = [11, 4, 3, 2, 10, 0, 0, 0]
cards = list("AKQJT987")

def bela(dom, someList):
	score = 0
	for i in someList:
		if i[1] == dom:
			score += dominant[cards.index(i[0])]
		else:
			score += notDominant[cards.index(i[0])]
	print(score)

N, D = input().split()
hands = [input() for i in range(4*int(N))]

bela(D, hands)