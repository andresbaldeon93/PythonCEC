# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 19:18:19 2020

@author: CEC
"""

from math import exp

ex=1

try:
    while True:
        print(exp(ex))
        ex *= 2
except OverflowError:
    print("El número es demasiado grande")