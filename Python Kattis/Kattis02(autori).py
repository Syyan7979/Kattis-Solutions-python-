def autori(someList):
	out = ""
	for i in someList:
		out += i[0]
	return out

someinpt = input().split("-")
print(autori(someinpt))