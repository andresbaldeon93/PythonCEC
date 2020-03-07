# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 19:15:29 2020

@author: CEC
"""

import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Quito"
dest = "Guayaquil"
key = "6sHAI2zouPSmc6kOQzoPyki4190uSVAF"

url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})

json_data = requests.get(url).json()
print(json_data)