def comparison(a, b):
	score = len(a)
	death = 10
	for i in b:
		if score == 0:
			print("WIN")
			break
		elif death == 0:
			print("LOSE")
			break
		else:
			if i in a:
				score -= a.count(i)
			else:
				death -= 1
word = input()
permutation = input()
comparison(word, permutation)