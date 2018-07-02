#!/usr/bin/python

#################################################################################
# Tool Name       : PasswordGenerator.py
#
# Author          : Tarig Mudawi 
#                   Dakota State University
#
# Tool Description: This tool generates random complicated passwords that the user 
#                   could use for his/her various applications or websites logins.
#                   The tool also verify user generated password by validating that
#                   all password characters meet specific criteria. 
#
################################################################################## 

import sys

import random

import re


def PasswordOptions():
    '''Decide whether you need a new password or you like to validate your password'''

    ans=True
    while ans:
        print("""
        1. Create New Password.
        2. Validate My Password.      
        3.Exit/Quit
        """)
    
        ans=raw_input("Please select an option\n")
       
        if ans=="1":

            print("\nCreating new password for you...")

            GeneratePassword()

            continue

        elif ans=="2":

            print("\n Validadting your password...")

            ValidatePassword()

            continue

        elif ans=="3":

            print("\n Exiting...") 
            break
            ans = None

        else:
            print("\n Not Valid Choice Try again")
            


def ValidatePassword():
    '''Validate User Generated Password'''

    while True:

        password = raw_input("Enter a password: ")

        if len(password) < 8:

            print("Make sure your password is at lest 8 letters")

        elif re.search('[0-9]',password) is None:

            print("Make sure your password has a number in it")

        elif re.search('[a-z]',password) is None: 

            print("Make sure your password has a small letter in it")

        elif re.search('[A-Z]',password) is None: 

            print("Make sure your password has a capital letter in it")

        elif re.search('[~!@#$%^&*()]',password) is None:

            print("Make sure to use at least one special character from this list: [~!@#$%^&*()]")

        else:

            print("Your password seems fine")

            break


def CheckPasswordLength(PasswordLength):
    '''Function to verify that password entered by the user is at least 8 characters'''

    while(1):

        if(PasswordLength < 8 ):

            PasswordLength = Length_Input("Password must be minimum of 8 characters. Please choose a larger length.\n")

        elif(PasswordLength >= 8 and PasswordLength <= 10):

            print "Password Length Accepted, your password is generated below.\n"

            break

        elif(PasswordLength > 24 ):

            PasswordLength = Length_Input("Password is too long please choose, maximum length is 24 characters. \n")

        else:

            print "Strong Password Generated.\n"

            break

    return PasswordLength

def Length_Input(message):
    '''Validate length entered by the user'''

    try:
        ret = int(input(message))
        return ret
    except:
       return Length_Input("enter a number for the length\n")
 

def GeneratePassword():
    '''Generate a password based on user selected length.'''

    # Password is constructed from this list
    Char_List = "abcdefghijklmnopqrstuvwxyz!@#$%^&*()"

    my_password_length = Length_Input("Enter a password length\n")


    # Call CheckPasswordLength function to verify the length
    my_password_length = CheckPasswordLength(my_password_length)

    my_password = ""
    
    
    for i in range(my_password_length):

        next_index = random.randrange(len(Char_List))

        my_password = my_password + Char_List[next_index]
    
    # replace 1 or 2 characters with a number
    for i in range(random.randrange(1,3)):

        replace_index = random.randrange(len(my_password)//2)

        my_password = my_password[0:replace_index] + str(random.randrange(10)) + my_password[replace_index+1:]
    
    # replace 1 or 2 letters with an uppercase letter
    for i in range(random.randrange(1,3)):

        replace_index = random.randrange(len(my_password)//2,len(my_password))

        my_password = my_password[0:replace_index] + my_password[replace_index].upper() + my_password[replace_index+1:]
    
    print(my_password)


def main():

    # create a new password or check password validity
    PasswordOptions()
    

if __name__ =="__main__":
    main()