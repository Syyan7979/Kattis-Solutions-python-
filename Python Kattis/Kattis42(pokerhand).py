def poker(someList):
	hand = {}
	for i in someList:
		if f"{i[0]}" in hand:
			hand[f"{i[0]}"] += 1
		else:
			hand[f"{i[0]}"] = 1

	vals = list(hand.values())
	return max(vals)

pokerHand = input().split()
print(poker(pokerHand))