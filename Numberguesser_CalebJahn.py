# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 09:02:51 2024

@author: Caleben Jahn
"""
import random
number= random.randint(1,101)
tries= 0
keepgoing = True
while(keepgoing):
    tries +=1
    guess= input("pick a number between 1 and 100")
    
    if guess.isdigit():
    
        if int(guess) > number :
                print("too high, try again")
        
        elif int(guess) < number :
                print ("too low, try again")
    
        elif int(guess) == number :
                print("Great job, you got it!")
                keepgoing = False
    else:
        print("Type a number my guy")
    
    
    
    if tries >= 7:
        print("too many tries, start over")  
        keepgoing = False
#when making guesses, do not press the space bar, just type the number.
#Couldn't figure out how to make it not cry when I pressed space. 
    