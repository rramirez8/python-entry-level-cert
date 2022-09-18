y = 5

def setx(z):
	x = z
	global y
	global a
	y = x
	a = 7

print("Y before setx: ", y)
setx(10)
print("Y after setx: ", y)
print("A after setx: ", a)

