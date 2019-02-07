# -*- coding: UTF-8 -*-
'''
    Created on 2018-1-28
    github repo Crawler
    @author: Manyao Peng
'''
from __future__ import (division, print_function, absolute_import, unicode_literals)

import os
import time
import requests

base_url = "https://api.github.com"

def gh_request(endpoint, retries=0):
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "GH_Crawler",
        "Authorization":"token MyToken",
        "Content-Type":"application/json",
    }
    
    try:
        r = requests.get(base_url + endpoint, headers=headers)
    except requests.exceptions.ConnectionError:
        if retries < 10:
            print("Retrying {0}".format(endpoint))
            return gh_request(endpoint, retries=retries+1)

    if r.status_code != requests.codes.ok:
        if r.status_code == 403:
             # This probably means that the rate limit was reached.
             # Wait for rate limit to reset and then re-submit the request.
             remain = int(r.headers["X-RateLimit-Remaining"])
             if remain < 1:
                 reset = int(r.headers["X-RateLimit-Reset"]) - time.time()
                 print("Waiting {0} seconds for rate limit to reset...".format(reset))
                 time.sleep(max(1.0, reset))
                 return gh_request(endpoint)

        r.raise_for_status()

    return r
