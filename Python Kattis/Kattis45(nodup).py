def nodup(someList):
	d = {}
	ans = True
	for i in someList:
		if i in d:
			ans = False
			break
		else:
			d[i] = 1
	return ans

if nodup(input().split()):
	print("yes")
else:
	print("no")