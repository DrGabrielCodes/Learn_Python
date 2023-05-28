def add(x, y):
   print(x+y)

add(20,30)

def subtract(x, y):
   print(x-y)

num3 = "75"
num4 = 77.3
try:
   print( num4)
   print("successfully printed")
except TypeError:
   print("An error ocurred due to a TypeError")

print("hello")

num5 = 75
num4 = 77.3
try:
   print(num5+num4)
   print("successfully printed")
except:
   print("An error ocurred due to a TypeError")

try:
   print(num4)
   print("successfully printed")
except TypeError:
   print("An error ocurred due to a TypeError")
finally:
   print("I just have to run no matter what happens")
