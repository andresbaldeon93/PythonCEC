# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 19:15:29 2020

@author: CEC
"""

import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "6sHAI2zouPSmc6kOQzoPyki4190uSVAF"

while True:
    orig = input("Starting location:" )
    if orig=="quit" or orig == "q":
        break
    dest = input("Destination: ")
    if dest=="quit" or dest == "q":
        break
    url = main_api + urllib.parse.urlencode({"key":key,"from":orig,"to":dest})

    print("URL: " + (url))
    json_data= requests.get(url).json()
    #print(json_data)

    json_status = json_data["info"]["statuscode"]

