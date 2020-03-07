# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 11:23:14 2020

@author: CEC
"""

import numpy as np

a=np.array([1,2,3])
print(a)

b=np.array([(1,2,3),(4,5,6)])
print(b)

c=np.array([(1,2,3),(4,5,6),(7,8,9)])
print(c)

array = np.array([[1,2,3,4],[5,6,7,8]],dtype=np.int64)
print(array)

unos=np.ones((3,4))
print(unos)

ceros=np.zeros((3,4))
print(ceros)

aleatorios=np.random.random((2,2))
print(aleatorios)

vacia=np.empty((3,2))
print(vacia)

full=np.full((2,2),8)
print(full)

#Crear una matriz con valores espaciados uniformemente
espacio1 = np.arange(0,30+1,5)
print(espacio1)

#Matriz con 5 valores que se encuentren entre 0 y 2
espacio2 = np.linspace(0,2,5)
print(espacio2)

#Matriz identidad
identidad1 = np.eye(4,4)
print(identidad1)

identidad2 = np.identity(4)
print(identidad2)

#Conocer dimensión de una matriz
a=np.array([(1,2,3),(4,5,6)])
print(a.ndim)

#Conocer el tipo de datos
print(a.dtype)
#Conocer el tamaño y forma de la matriz
print(a.size)
print(a.shape)

#Cambio de forma de una matriz
c= np.array([(8,9,10),(11,12,13)])
print(a)
print("\n"*2)
a=a.reshape(3,2)
print(a)


a=np.array([(1,2,3,4),
            (3,4,5,6)])
print(a)
print("\n"*1)
print(a[1,2])
print("\n"*1)
print(a[0:,2])


x = np.array([(1,2,3),
              (3,4,5)])
y= np.array([(1,2,3),
             (3,4,5)])
print(x+y)
print("\n")
print(x-y)
print("\n")
print(x*y)
print("\n")
print(x/y)
