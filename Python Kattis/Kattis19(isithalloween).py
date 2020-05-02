def halloween(m, d):
	if m == "OCT" and d == 31:
		print("yup")
	elif m == "Dec" and d == 25:
		print("yup")
	else:
		print("nope")

month, date = input().split()
halloween(month, int(date))