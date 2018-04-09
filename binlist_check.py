#!/usr/bin/python
#coding: utf-8

import requests
import json
import time

url = 'https://lookup.binlist.net/'
b = raw_input("Insert a bin: ")
headers = {'Accept-version': '3'}

http = requests.get(url+b,headers=headers)
content = http.content
json_data = json.loads(content)
for i in json_data.keys():
    print (i+" : "+str(json_data[i]))
