from xml.dom import minidom

from bs4 import BeautifulSoup


# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 09:37:00 2023

@author: jwill
"""

filepath = 'materials data base/materials.xml'

 
 
# Reading the data inside the xml
# file to a variable under the name
# data
with open(filepath, 'r', encoding="utf8") as f:
    data = f.read()
 
# Passing the stored data inside
# the beautifulsoup parser, storing
# the returned object

file = BeautifulSoup(data, "xml")
mls = file.findChild('Materialfile_LaserSim')
matdb = mls.findChild('list_of_materials')

for c in matdb.children:
    
    if c.name == None: continue
    
    print(type(c))
    
    print(c.name)
    print(c.text)
    
    break
