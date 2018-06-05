#Answer 5
#Import Error
'''The ImportError is raised when an import statement has trouble successfully importing the specified module.
 Typically, such a problem is due to an invalid or incorrect path, which will raise a ModuleNotFoundError'''

try:
    import gw_utility.Book
except:
    print("cannot import file")
	
#ValueError
'''The ValueError is in case if we give invalid inputs for example string in case of integer'''

try:
	a=int(input("Enter an integer value:"))
	print("Correct Input")
except:
	print("Exception:", TypeError)

#IndexError
'''It occurs when we try to access an index of a sequence which does not exist'''

l=[1,2,3]
try:
	print(l[3])
except:
	print("Index Error")
	
 

 
