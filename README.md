Tool Description:
===

This tool is used to help users generate complex passwords that they need for their applications and websites.
The tool is intended to help regular non-technincal users to generate or validate passwords.


Technical Specification:
===

* Windows 10 Operating System.
* Python 2.7
* No other dependencies or third-party library needed.


Usage:
===

As illustrated below, the user simply needs to specify the word python followed by the script name.

C:\Python27>python PasswordGenerator.py

When selecting option 1 to generate a password the script starts with by validating the password length, for instance 
if the user enters a password length of 7 or less characters then he/she got prompted to enter a bigger length. On the other 
hand if she/he entered a passowrd of length that is more than 24 characters he will got prompted to enter a length that is less 
than 24 characters.
When selecting option 2 the user can validate a password, in this scenario the script checks that the password has an upper case,
a digit and a special character. If any of these is missing the user got prompted to add the missing criteria to his password. 
If the password satisfies all criterion the user notified that his password is fine. Finally option 3 is to exit the script.
 

 

