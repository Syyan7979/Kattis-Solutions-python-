A, B = [int(i) for i in input().split()]
if A-B > 0:
	if A-B != 1:
		print(f"Dr. Chaz needs {A-B} more pieces of chicken!")
	else:
		print(f"Dr. Chaz needs {A-B} more piece of chicken!")
else:
	if B-A != 1:
		print(f"Dr. Chaz will have {B-A} pieces of chicken left over!")
	else:
		print(f"Dr. Chaz will have {B-A} piece of chicken left over!")