def equivalence(g, s, c):
	total = 3 * g + 2 * s + c
	vC = [("Province", 8), ("Duchy", 5), ("Estate",2)]
	tC = [("Gold", 6), ("Silver", 3), ("Copper", 0)]

	v = ""
	t = ""
	for i in vC:
		if i[1] <= total:
			v += i[0]
			break
	for i in tC:
		if i[1] <= total:
			t += i[0]
			break
	if v == "":
		print(t)
	else:
		print(f"{v} or {t}")

G, S, C = [int(i) for i in input().split()]
equivalence(G, S, C)