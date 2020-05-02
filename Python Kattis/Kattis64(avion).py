def avion(someList):
	out = ""
	for i in range(5):
		if "FBI" in someList[i]:
			out += f"{i+1} "
	if out == "":
		print("HE GOT AWAY!")
	else:
		print(out)
avion([input() for i in range(5)])