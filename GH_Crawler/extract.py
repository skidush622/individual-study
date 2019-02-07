# -*- coding: UTF-8 -*-
'''
    Created on 2018-1-28
    github repo Crawler
    @author: Manyao Peng
'''

import os
import time
import json
import re

def extract(readme):
    array = []
    pat = re.compile('(?<=\>).*?(?=\<)')
    flag = False
    file_object = open(readme,'rU')
    try:
       for line in file_object:
           if(line.startswith("## Installation") or line.startswith("Installation")):
              flag = True
           elif(flag and (line.startswith("## ") or line.startswith("======"))):
              flag = False
           if(flag):
               elem = line.rstrip('\n')
               if(elem):
                   array.append(elem)
    finally:
       file_object.close()
    return array
