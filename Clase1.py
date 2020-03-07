# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 09:19:10 2020

@author: CEC
"""

class Employee:
    'Common base class for all employees'
    empCount = 0
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
    def displayCount(self):
        print ("Total Employee %d" %Employee.empCount)
        
    def Employee(self):
        print ("Name: ",self.name,", Salary: ",self.salary)
        
###INSTANCIAMOS LA CLASE
emp1 = Employee("Zara",2000)
emp2 = Employee("Manni",5000)
emp3 = Employee("Anabel",2500)
emp4 = Employee("Lucia",3000)
emp5 = Employee("Monica",4000)
emp6 = Employee("Patricio",4500)

emp5.Employee()



