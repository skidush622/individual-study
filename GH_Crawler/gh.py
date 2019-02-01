# -*- coding: UTF-8 -*-
'''
    Created on 2018-1-28
    github repo Crawler
    @author: Manyao Peng
'''
import os
import time
import requests

base_url = "https://api.github.com"

def gh_request(endpoint, method="GET", retries=0, **kwargs):
    payload = dict(**kwargs)
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "pengm/GH_Crawler",
        "Authorization":"token 6f6cebd113a20f4bb71861beaa1657e0573bfbd0",
        "Content-Type":"application/json",
    }
    try:
        r = getattr(requests, method.lower())(base_url + endpoint, params=payload, headers=headers)

    except requests.exceptions.ConnectionError:
        if retries < 10:
            print("Retrying {0}".format(endpoint))
            return gh_request(endpoint, method=method, retries=retries+1, **kwargs)

    if r.status_code != requests.codes.ok:
        if r.status_code == 403:
             # This probably means that the rate limit was reached.
             # Wait for rate limit to reset and then re-submit the request.
             remain = int(r.headers["X-RateLimit-Remaining"])
             if remain < 1:
                 reset = int(r.headers["X-RateLimit-Reset"]) - time.time()
                 print("Waiting {0} seconds for rate limit to reset...".format(reset))
                 time.sleep(max(1.0, reset))
                 return gh_request(endpoint, method=method, **kwargs)

        r.raise_for_status()

     return r
