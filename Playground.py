from bs4 import BeautifulSoup as BF
import re
import requests as req
import sqlite3
karo = {1: {"скайокер": ["12:30"]}, 2: {"один дома" : ["13:50"]}}
cinemas = {"cinema's name": {"metro" : "marino", "data-id" : "43"}, "uc" :{"metro" : "bunino",  "data-id" : "54"}}
checker = {1: "43", 2: "54"}
#for i in karo:
 #   print(karo[i].keys())
if "54" in checker.values():
    print("yes")
for i in cinemas.values():
    print(i.get("data-id"))











