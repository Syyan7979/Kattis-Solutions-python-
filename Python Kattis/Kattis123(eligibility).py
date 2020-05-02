def eligibility(name, a, b, course):
	ps = [int(i) for i in a.split("/")]
	bd = [int(i) for i in b.split("/")]
	if ps[0] >= 2010 or bd[0] >= 1991:
		return name, True
	elif int(course) / 5 > 8:
		return name, False
	else:
		return name, "coach petitions"
n = int(input())
for i in range(n):
	nm, yr1, yr2, c = input().split()
	Name, ans = eligibility(nm, yr1, yr2, c)
	if ans and ans != "coach petitions":
		print(Name, "eligible")
	elif not ans:
		print(Name, "ineligible")
	else:
		print(Name, ans)