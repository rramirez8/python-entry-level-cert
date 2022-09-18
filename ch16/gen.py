def gen_range(stop, start=1, step=1):
	num = start
	while num <= stop:
		yield num
		num += step

for num in gen_range(10):
	print("The number is: ", num)

generator1 = gen_range(20)
gen_list = list(generator1)
print(gen_list)

def gen_fib():
	a, b = 0, 1
	while True:
		a, b = b, a + b
		yield a

fib1 = gen_fib()
print(next(fib1))
print(next(fib1))
print(next(fib1))
print(next(fib1))
print(next(fib1))
print(next(fib1))
print(next(fib1))

