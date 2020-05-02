def fuck(someList):
	print(someList[0]+someList[1])
n = int(input())
for i in range(n):
	ans = input()
	if ans == "P=NP":
		print("skipped")
	else:
		fuck([int(i) for i in ans.split("+")])