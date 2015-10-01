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
key=input("Key: ")
messagelist=[]
for x in message:
    messagelist.append(associations.find(x))
keylist=[]
for x in key:
    keylist.append(associations.find(x))
sumlist=[]
for x in range(0,len(message)):
    sumlist.append(keylist[x]+messagelist[x])
for x in sumlist:
    print(associations[x])


#if inp=="e":
    
if inp=="q":
    print("Goodbye!")