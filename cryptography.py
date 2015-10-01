"""
cryptography.py
Author: Adam Pikielny
Credit: http://www.tutorialspoint.com/python/string_len.htm

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
import sys

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
j=0
while len(key)<len(message):
    key+=(key[j])
    j+=1

for x in key:
    keylist.append(associations.find(x))
    
if inp=="e":
    sumlist=[]
    for x in range(0,len(message)):
        sumlist.append(keylist[x]+messagelist[x])
    for x in sumlist:
        sys.stdout.write(associations[x%85])

if inp=="d":
    difflist=[]
    for x in range(0,len(message)):
        difflist.append(keylist[x]-messagelist[x])
    for x in difflist:
        sys.stdout.write(associations[x%85])
    
if inp=="q":
    print("Goodbye!")