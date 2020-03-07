# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

str1="Cisco"
str2="Networking"
str3="Academy"
space=" "
print(str1+space+str2+space+str3)
print(str1,str2,str3)

first_name = input("Whats is your first name?")
print("Hello "+first_name+"!")

result = input("Ingrese nombre, apellido,ubicación y teléfono: ")
div=result.split(" ")
r0=div[0]
r1=div[1]
r2=div[2]
r3=div[3]
space=" "
print(r0+space+r1+space+r2+space+r3)

#SENTENCIA IF
nativeVLAN = 1
dataVLAN = 100
if nativeVLAN == dataVLAN:
    print("The native VLAN and the dataVLAN are the same.")
else:
    print("The native VLAN and the dataVLAN are different.")
    
aclNum= int(input("What is the IPv4 ACL number? "))
if aclNum >= 1 and aclNum <= 99:
    print("This is a standard IPv4 ACL")
elif aclNum >= 100 and aclNum <= 199:
    print("this is a extended IPv4 ACL")
else:
    print("This is not a standard or extended IPv4 ACL")

#SENTENCIA FOR
devices=["R1","R2","R3","S1","S2"]
for item in devices:
    print(item)

for item in devices:
    if "R" in item:
        print(item)
#AÑADE VALOR A UNA LISTA        
switches=[]
for item in devices:
    if "S" in item:
        switches.append(item)
print(switches)

#SENTENCIA WHILE
x=input("Enter a number to count to: ")
x=int(x)
y=1
while y<=x:
    print(y)
    y=y+1
    
#BREAK
x=input("Enter a number to count to: ")
x=int(x)
y=1
while True:
    print(y)
    y=y+1 
    if y>x:
        break

#SENTENCIA 
while True:
    x=input("Enter a number to count to: ")
    if x == 'q' or x == 'quit':
        break
    x=int(x)
    y=1
    while True:
        print(y)
        y=y+1 
        if y>x:
            break    
        
#OTROS TIPOS DE FOR
#1
for i in range(5):
    print(i+1)
    
#2
result=0
n=5
for i in range(1,n+1):
    result+=i
print(result)

#3
for i in range(10,0,-2):
    print(i)