#------------------
def fib(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	
	return fib(n-2) + fib(n-1)

#------------------

fib_position = int(input("Which fibonacci position would you like to calculate? "))
fib_value = fib(fib_position)
print(f"The value for fibonacci position {fib_position} is: {fib_value}")

# recursion in python is not optimized so use is sparingly and with caution
