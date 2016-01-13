def fib(max):
	n, a, b = 0, 0, 1
	while n < max:
		yield b
		a, b = b, a + b
		n = n + 1
	return 'done'


n = input("Please input the level of Fib\n")
for i in fib(int(n)):
	print(i)
