def judge(a, b):
	if a == b:
		if a == 0:
			print("Not a moose")
		else:
			print(f"Even {a+b}")
	else:
		if a > b:
			print(f"Odd {2*a}")
		elif a < b:
			print(f"Odd {2*b}")
			
A, B = [int(i) for i in input().split()]
judge(A, B)