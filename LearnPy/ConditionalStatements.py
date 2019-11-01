# This is my program to check conditional statements
user_number = input("enter your number")
if user_number.isdigit():
    print("user input is number")
elif user_number.islower():
    print("user input is lower string")
elif user_number.isupper():
    print("user input is upper string")
else:
    print("no character")