# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 18:37:15 2020

@author: CEC
"""

def readint(prompt, min, max):
    
    x = input(prompt)
    try:
        if int(x)>min:
            if int(x)<max:
               return x 
    except Exception:
        print("wrong input")
    else:
        print("Error: the value is not within permitted range (min..max)")


v = readint("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)
