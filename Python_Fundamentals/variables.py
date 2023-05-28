#Variables are containers that store values or objects.
# They are usually numbers and strings. They can also be custom created using classes.

#Numbers can either be a float or an integer. 
#A float is made of two or more literal numbers seperated by a decimal point.
myfloat = 56.89
anotherfloat = 8834.62

#An integer is a whole number without a decimal point
myInteger = 4847
anotherInteger = 65


#Python treats both floats and integers as numbers and thus can perform mathemathical operations on both
x = 400
y = 44
print(x + y)  
print(x - y)
print(x * y)
print(x / y)

#STRINGS****************
#Strings are a combination of characters (numbers, letters and special characters) enclosed by single or double quotes
# String examples
myString = "Programming" 
anotherString = 'Awesome'
print(myString)
#strings can be concatenated together using the plus sign (+)
print(anotherString + " "+ myString)

#A better way to do this is to use the format built-in function
print("{0} is {1}".format(myString, anotherString))



