def basketball(someString):
	aStak = 0
	bStak = 0
	for i in range(0, len(someString), 2):
		if someString[i] == "A": aStak += int(someString[i+1])
		else: bStak += int(someString[i+1])
		if aStak >= 11 and aStak - bStak >= 2:
			print("A")
			break
		elif bStak >= 11 and bStak - aStak >= 2:
			print("B")
			break
basketball(input())