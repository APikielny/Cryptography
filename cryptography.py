"""
cryptography.py
Author: <your name here>
Credit: <list sources used, if any>

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
inp=input("Enter e to encrypt, d to decrypt, or q to quit: ")
while inp!="e" and inp!="d" and inp!="q":
    print("Did not understand command, try again. \n")
    inp=input("Enter e to encrypt, d to decrypt, or q to quit: ")
message=input("Message: ")
if inp=="e":
    
if inp=="q":
    print("Goodbye!")