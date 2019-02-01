# -*- coding: UTF-8 -*-
import sys
import os
import urllib
import re, json, operator
import http.client

def BingSearch(queryStr):
        headers = {
             # Request headers
            'Ocp-Apim-Subscription-Key': '<replace with primary key>',#######
        }
        params = urllib.parse.urlencode({
            # Request parameters
            'q': queryStr,
            'count': '10',
            'offset': '0',
            'mkt': 'en-us',
            'safesearch': 'Moderate',
        })

        # get search results
        try:
            conn = http.client.HTTPSConnection('api.cognitive.microsoft.com')
            conn.request("GET", "/bing/v7.0/search?%s" % params, "{body}", headers)
            response = conn.getresponse()
            data = response.read()
            fh = open("response.txt", 'wb')
            fh.write(data)
            fh.close()
            fh = open("response.txt",'r+')
            str = fh.read()
            fh.close()
            #response to Json structure
            json_data = json.loads(str)
            #get the url
            url = json_data["webPages"]["value"][0]["deepLinks"][0]["url"]
            conn.close()
            return url
        except Exception as e:
            print("[Errno {0}] {1}".format(e.errno, e.strerror))
