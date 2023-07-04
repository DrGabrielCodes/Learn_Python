"""
Write a program named first_letter.py that prompts the user for input
with the string "Tell me your password:". The program should then
determine the first letter of the user’s input, convert that letter to uppercase,
and display it back.
"""

password = input("Tell me your password: ")


first_letter = password[0]
print(first_letter.upper())