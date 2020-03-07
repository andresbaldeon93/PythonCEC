# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 18:25:04 2020

@author: CEC
"""
def reciproco(n):
    try:
        n = 1 / n
    except ZeroDivisionError:
        print("Division Fallida")
        return None
    else:
        print("Todo salió bien")
        return n
    finally:
        print("Es el momento de decir adiós")
        return n
    
print(reciproco(2))
print(reciproco(0))
     