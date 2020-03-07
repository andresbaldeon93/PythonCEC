# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 12:20:59 2020

@author: CEC
"""

import pandas as pd
titulos = pd.read_csv('data/titles.csv' )
print(titulos.head(100))
print("\n"*2)
elenco = pd.read_csv('data/cast.csv', encoding='utf-8')
print(elenco.head(10))
#Cuantas peliculas estan listadas en el dataframe de títulos?
print(len(titulos))

#Cual fue la primer pelicula hecha y titulada Romeo y Julita
print(titulos[titulos.title=='Romeo and Juliet'].sort_values('year').head(5))
#Listar las que contengan la palabra exorcista de la mas vieja a la mas reciente
print(titulos[titulos.title.str.contains("Exorcist")].sort_values('year'))

print(titulos[titulos.title.str.contains("Taxi Driver")].sort_values('year'))
print(titulos[titulos.year.between(1980,2000)]) #mejor utilizar comparadores bit a bit
print(len( titulos[ (titulos.year >= 1980) & (titulos.year <= 2000)]))
print(len(elenco[elenco.title=="Godfather"]&elenco.count(elenco.character)))

