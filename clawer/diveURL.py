# -*- coding: UTF-8 -*-

import sys
import os
from urllib import request
from bs4 import BeautifulSoup
import subprocess
import re, json, operator

def getLink(url):
    response = request.urlopen(url)
    content = response.read().decode('utf-8')
    links = []
    bsObj = BeautifulSoup(content, "html.parser") # not lxml
    for node in bsObj.find_all("a"):
        links.append(node["href"])
    return links[8]

def getInfo(link):
    fh = open("install.txt", 'w')
    fh.write(link)
    fh.close()
    if(re.match(".*pkg", link)==None):
       link = getLink(link)
