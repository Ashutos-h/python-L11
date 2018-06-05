#Answer 1
#The exception in this program is ZeroDivisionError


a=3
try:
	if a<4:
		a=a/(a-3)
		print(a)
except:
	print("Cannot divide by zero")

	