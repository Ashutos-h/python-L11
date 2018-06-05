#Answer 2
#This program will cause IndexOutOfRange exception.

l=[1,2,3]
try:
	print(l[3])
except:
	print("Index out of range")
	