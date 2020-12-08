from random import *
import time

user_pass = input("Enter your password: ")

print(time.perf_counter())

password = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u','v', 
            'w', 'x', 'y', 'z','1','2','3','4','5','6','7','8','9','0',
            'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O',
            'P','Q','R','S','T','U','V','W','X','Y','Z', '!','@','#',"$",'%','^','&','*']

guess = ""

while (guess != user_pass):
    guess = ""
    for letter in range(len(user_pass)):
        guess_letter = password[randint(0, 69)]
        guess = str(guess_letter) + str(guess)
    

print(time.perf_counter())
    
print("Your password is",guess)