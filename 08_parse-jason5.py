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

    if json_status==0:
        print("API Status: "+str(json_status)+" = A successfull route call.\n")
        print("Directions from "+(orig)+" to "+(dest))
        print("Trip Duration: "+str(json_data["route"]["formattedTime"]))
        print("Kilometers: "+str(json_data["route"]["distance"]*1.61))
        print("Fuel (Gal): "+str(json_data["route"]["fuelUsed"]))
        print("=======================================")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"])+"("str("{:.2f}".format((each["distance"])*1.161))+" km"))
        print("=======================================\n")
        