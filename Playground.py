from bs4 import BeautifulSoup as BF
import re
import requests as req
import sqlite3
karo = {1: {"скайокер": ["12:30"]}, 2: {"бурунов дома" : ["13:50"]}}
cinemas = {"cinme": {"metro" : "marino", "data-id" : "43"}}
#for i in karo:
 #   print(karo[i].keys())
for i in cinemas.values():

    print(i.values())











