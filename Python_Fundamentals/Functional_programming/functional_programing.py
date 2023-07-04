#Functional programing is a method of programming that is focused on using functions to achieve tasks.and

#A vital aspect of functional programing is HIGHER-ORDER FUNCTIONS, these functions take other functions as an argument or return them as results

#For instance
def multiply_by_six(number):
    return number * 6           #This is a simple function that takes a numer as an inpurt and returns another number multiplied by 6

def apply_once(func, arg):
    return func(arg)            #This simply takes the function and does what the function says once

def apply_twice(func, arg):
    return func(func(arg))      #This simply takes the function as its argument and does its task twice

def apply_thrice(func, arg):
    return func(func(func(arg)))      #This simply takes the function and does its job threefold

print(multiply_by_six(10))

print(apply_twice(multiply_by_six, 5))
print(apply_thrice(multiply_by_six, 5))
