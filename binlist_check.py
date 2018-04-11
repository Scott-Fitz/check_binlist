#!/usr/bin/python
#coding: utf-8

import requests
import json
import time

url = 'https://lookup.binlist.net/'
#b = raw_input("Insert a bin: ")
headers = {'Accept-version': '3'}
#bins = open('/kalimac/Documents/python_scripts/check_binlist/bin_list_num.txt', 'rb')
#b = int(bins.readline()
with open('/kalimac/Documents/python_scripts/check_binlist/bin_list_num.txt') as line:
    for b in line:
#f = open('/kalimac/Documents/python_scripts/check_binlist/bin_list_num.txt', 'rb+')
        #b = f.readline()
        time.sleep(1)
        b = b.strip('\n')
        print('-'*10)
        print(b)
        print('-'*10)
        http = requests.get(url+b,headers=headers)
        content = http.content
        json_data = json.loads(content)
        for i in json_data.keys():
            print (i+" : "+str(json_data[i]))
