# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 19:15:29 2020

@author: CEC
"""

import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Quito"
dest = "Esmeraldas"
key = "6sHAI2zouPSmc6kOQzoPyki4190uSVAF"
url = main_api + urllib.parse.urlencode({"key":key,"from":orig,"to":dest})

print("URL: " + (url))
json_data= requests.get(url).json()
#print(json_data)

json_status = json_data["info"]["statuscode"]

if json_status == 0:
    print("API Status: " + str(json_status) + " = A successful route call.\n")