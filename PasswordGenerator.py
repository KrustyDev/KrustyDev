#Application to randomly generate a password
import random

s = "abcdefghijklmnopqrstuwxyz1234567890ABCDEFGHIJKLMNOPQRSTUWXYZ!@$%^&*()_-+[];/';.,"


#Example Output
#!8MAQ7)z(D$I@HmL
#u1U_IGw+pyAdcCl;
#e^85d.Jz6X-PhH%E
#!x_)C^Sa6q5-GlFb
while 1:
    for x in range(0,15):
        password = ''
        p = random.choise(s)
        password = password + p
print(password)
    

