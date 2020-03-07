# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 10:56:06 2020

@author: CEC
"""

def fibonacci(n):
    a, b = 0,1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
#fibonacci(20)