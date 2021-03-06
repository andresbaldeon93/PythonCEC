# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 08:40:07 2020

@author: CEC
"""

# Python program to check if year is a leap year or not

year = 2000

# To get year (integer input) from the user
# year = int(input("Enter a year: "))


def isYearLeap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True
   
def daysInMonth(year,month):
	if year < 1900 or month < 1 or month > 12:
		return None
	days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	res  = days[month-1]
	if month == 2 and isYearLeap(year):
		res = 29
	return res
print(daysInMonth(2020,1 ))

def dayOfYear(year, month, day):
	days = 0
	for m in range(1, month):
		md = daysInMonth(year, m)
       ### print(md)
		if md == None:
			return None
		
		days += md
	
	md = daysInMonth(year, month)
	if day >= 1 and day <= md:
		return days + day
	else:
		return None

print(dayOfYear(2020, 2, 22))

