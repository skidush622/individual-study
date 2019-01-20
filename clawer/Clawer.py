# -*- coding: UTF-8 -*-
'''
    Created on 2018-11-10
    Clawer for collecting dependencies install scripts
    @author: Manyao Peng
'''
import sys
import os
import urllib
import subprocess
from BingSearch import *
from diveURL import getLink, getInfo

if __name__ == '__main__':
    flag = True
    while flag:
        tip = str("\n\n=========== What to install ============\n\n")
        target = input(tip)
        cmd_line = target + " -v"
        try:
            ret = subprocess.check_output(cmd_line)
        except Exception as e:
            print ("Not install " + target + "\n")
            print ("Start to collect installation of " + target + "\n")
            query = "install " + target
            url = BingSearch(query)
            link = getLink(url)
            getInfo(link)
        print ("Completed\n")
