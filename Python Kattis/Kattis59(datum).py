d = {1 : "Monday",
	 2 : "Tuesday",
	 3 : "Wednesday",
	 4 : "Thursday",
	 5 : "Friday",
	 6 : "Saturday",
	 7 : "Sunday"}

def datum(day, month):
	if month > 8:
		days = day + (30*(month-1) + ((month-1)//2 + 1)) - 2
		date = days % 7
		if date > 4:
			print(d[(date+3)-7])
		else:
			print(d[date+3])
	elif month < 3:
		if month == 1:
			date = day % 7
			if date > 4:
				print(d[(date+3)-7])
			else:
				print(d[date+3])
		else:
			date = (day + 31) % 7
			if date > 4:
				print(d[(date+3)-7])
			else:
				print(d[date+3])
	else:
		if (month - 1) % 2 == 0:
			days = day + (30*(month-1) + ((month-1)//2)) - 2
			date = days % 7
			if date > 4:
				print(d[(date+3)-7])
			else:
				print(d[date+3])
		else:
			days = day + (30*(month-1) + ((month-1)//2 + 1)) - 2
			date = days % 7
			if date > 4:
				print(d[(date+3)-7])
			else:
				print(d[date+3])
a, b = [int(i) for i in input().split()]
datum(a, b)