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



  #USING ESCAPING SLASHES AND SPECAIL CHARACTERS
  # Some special features such as 
  # a new line represented with \n
  # a tab space represented with \t
  # 
  #  Examples
first_line = "Myopia is can be degenerative or pathological. "
second_line = "Individuals with myopia need spectacle prescription."

print(first_line + second_line) # This prints both sentences on the same line
print(first_line +"\n" + second_line) # This prints both sentences on the separate lines. The second sentence is moved to a new line.
print(first_line +"\t" + second_line) # This prints both sentences on the same line, with a tab space separating the two sentences.

#Sometimes when using strings you may want to use strings with back slashes in their raw form without it operating those special functions.
# All you have to do is include the key letter r infront of the string. This allows the interpreter to read that string as a raw continous set of characters. 
#For instance:
filename = "c:gabrelpc\name\videos" #Here, \n and \v are treated as special backslash letters/functions.
print(filename)

#To aviud this problem, use the letter r befor the string. 
filename2 = r"c:gabrielpc\name\videos"
print(filename2) # This prints the strings exactly as typed in.

#STRING literals
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

print("""
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

#INDEXING
# Strings can be indexed (subscripted), with the first character having index 0. There is no separate character type; a character is simply a string of size one:
first_line = "Myopia is can be degenerative or pathological"
print(first_line[0]) #This prints the letter M
print(first_line[1]) #This prints the letter y

#Indices may also be negative numbers, to start counting from the right:
print(first_line[-1]) #This prints the letter l
print(first_line[-2]) #This prints the letter a


#SLICING 
#String parts can be sliced to get parts of the strings
print(first_line[0:3]) #This prints the first 3 letters/characters of the string, starting from position 0 to 2, it excludes the last number
print(first_line[2:13]) #This prints the 11 letters/characters of the string, starting from index 2 to 12, it excludes the last index ie 13
print(first_line[0:6]) #This prints the first 6 letters of the string, starting from index 0 to 5, it excludes the last number

#If the begining slicing number is omitted, python assumes it to be 0, so the slicing starts from the first charcater of the string
print(first_line[:3]) #This prints the first 3 letters/characters of the string, starting from position 0 to 2, it excludes the last number
print(first_line[:6]) #This prints the first 6 letters of the string, starting from index 0 to 5, it excludes the last number

#If the ending slicing number is omitted, python assumes it to be the last character of the string, so the slicing stops at the last character of the string
print(first_line[10:]) #This prints the letters of the string from index 6 to the last character



#LENGTH of the string is the total number characters in a given string


