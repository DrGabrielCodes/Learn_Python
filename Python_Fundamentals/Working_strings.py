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

  # USING ESCAPING SLASHES AND SPECAIL CHARACTERS
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
#Using triple quotes allows you to create a string literal whic is printed exactly as typed, maintaining all the struscture and double quoutes
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
#the len() function is used to get the length of a sting

text1 = "an awesome "
text2 = "text is here"
concat_text = text1 + text2  #This combines text1 and text2
print(len(concat_text))


main_text = "Bazinga"
new_text = main_text[2:6]
print(new_text)

#MANIPULATING STRINGS
#Strings can manipulated using string methods. These methods usually start with a dot(.)

main_text.lower()  #converts every item of the string to a lower case
main_text.upper()  #converts every item of the string to an upper case

Myopia_rx = "    Individuals with myopia need spectacle prescription   "
right_strip_myopia_rx = Myopia_rx.rstrip() # removes whitespace from the right side of a string
left_strip_myopia_rx = Myopia_rx.lstrip() # removes whitespace from the lefft side of a string
both_strip_myopia_rx = Myopia_rx.strip() # removes whitespace from the both right and left sides of a string


print(right_strip_myopia_rx)
print(left_strip_myopia_rx)
print(both_strip_myopia_rx)


#TO DETERMINE IF A STRING starts with or ends with certain characters, use the string methods .startwith() and .endswith().
#Note this method is case sensitive
 
word = "Exceellent programme"
print(word.startswith("ex")) #This prints False because the phrase starts with E not e.
print(word.startswith("Ex"))  #This evaluates to True
print(word.endswith("ex"))    #This evaluates to False


#PROGRAM THAT REMOVES WHITE SPACES

string1 = " Filet Mignon"
string2 = "Brisket "
string3 = " Cheeseburger "

print(string1.strip())
print(string2.strip())
print(string3.strip())


#PROGRAM THAT PRINTS OUT RESULT OF .startswith(Be)

string1 = "Becomes"
string2 = "becomes"
string3 = "BEAR"
string4 = " bEautiful"

print(string1.startswith("Be"))
print(string2.startswith("Be"))
print(string3.startswith("Be"))
print(string4.startswith("Be"))

#INTERACTING WITH USER INPUT
#The input() method is used to get an input from the user
#You can give it a prompt, to make it more user friendly
#For instance

Name = input("Enter your full name here: ")
Age = input("How old are you? : ")
#This is a very useful way to obtain information from users.

message = f"Hi {Name}, it's nice to finally meet you. You can call me SizaTech. I heard you are {Age}. "
print(message) #Here f is a special character used to format the text, more like a short form of using the .format() method.


shout_out_input = input("Which of your friends are you giving a shout out today? ")
shout_out = f"Whats up! {shout_out_input} your Gee {Name} asked us to give you a shout out today."

print(shout_out)

# A PROGRAM THAT TAKES AN INPUT AND RETURNS IT IN A UPPER CASE
print(shout_out_input.upper())

#A PROGRAM THAT DISPLAYS THE NUMBER OF CHARACTERS 
print(len(Name))







