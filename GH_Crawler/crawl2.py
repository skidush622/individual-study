# -*- coding: UTF-8 -*-
'''
    Created on 2018-1-28
    github repo Crawler
    @author: Manyao Peng
'''

import os
import time
import json
import traceback
from repos import get_dependency

if __name__ == '__main__':
    flag = True
    while flag:
        tip = str("\n\n=========== Enter github username ============\n\n")
        username = input(tip)
        tip = str("\n\n=========== Enter github repo name ============\n\n")
        repo = input(tip)
        print("\nretrieve dependencies....\n")
        if(username and repo):
            res = get_dependency(username, repo)
        if(res is False):
            print("already exists")
            continue
        tip = str("\n\n=========== install? (Y/N) ============\n\n")
        install = input(tip)
        if(install is 'Y'):
           if(res is 1):
               path = "./req/"+username+"/"+repo+"/requirements.txt"
               print("do pip install with " + path)
           else:
               path = "./req/"+username+"/"+repo+"/package.json"
               print("do npm install with " + path)
