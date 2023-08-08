from asyncio import ALL_COMPLETED
import random as r #need random lib

n = int(input("Enter length of password: "))

#create library for characters that will be included in 
#password:

all_characters = []
for a in range(32,127): #google says printable ASCII are 
   all_characters.append(chr(a)) #between dec 32 and 127

passwrd = ""
for a in range(0,n):#now password
   x = r.randint(0,94) #127-32 = 95 characters total therefore
   # 0-94 will be array index for all_characters array
   passwrd = passwrd+ all_characters[x]

print("Password : ", passwrd)






