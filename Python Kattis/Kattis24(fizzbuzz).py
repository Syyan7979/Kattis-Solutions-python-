def fizzBuzz():
	for i in range(1, n+1):
		if i % X == 0 and i % Y == 0:
			print("FizzBuzz")
		elif i % X == 0:
			print("Fizz")
		elif i % Y == 0:
			print("Buzz")
		else:
			print(i)

X, Y, n = [int(i) for i in input().split()]
fizzBuzz()