import string
import random
l=string.ascii_lowercase
u=string.ascii_uppercase
d=string.digits
s=string.punctuation
while True:
    p_l=int(input("Enter length of the the password:"))
    if p_l<6:
        print("password length should be more than 6.")
        continue
    else:
        break
c=l+u+d+s
pas=""
for i in range(p_l):
    pas+=random.choice(c)
print("The random password generated with the given length is: ",pas)