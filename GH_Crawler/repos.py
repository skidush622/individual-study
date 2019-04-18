# -*- coding: UTF-8 -*-
'''
    Created on 2018-1-28
    github repo Crawler
    @author: Manyao Peng
'''

import os
import json
import base64
import random
import requests

from gh import gh_request
from extract import extract

TOTAL_N_EST = 21300000

BASE_DIR = "./data"
try:
    os.makedirs(BASE_DIR)
except os.error:
    pass

def get_random_repos():
    i = random.randint(0, TOTAL_N_EST)
    r = []
    while not len(r):
        r = gh_request("/repositories?since=" + str(i)).json()
    return r

def get_dependency(username, repo):
    # Skip if this repo had already been downloaded.
    bp = os.path.join("./req", username+"/"+repo)
    if os.path.exists(bp):
        print(username+"/"+repo + " has already been downloaded. Skipping")
        return False
    
    print("Processing " + username+"/"+repo + " ...\n")

    # Save the information.
    try:
        os.makedirs(bp)
    except os.error:
        pass

    dependency=None
    try:
        r = gh_request("/repos/{0}/{1}/contents/requirements.txt".format(username, repo)).json()
    except requests.exceptions.HTTPError:
        print("No requirements.txt found\n")
    else:
        content = r.get("content", None)
        dependency = base64.b64decode(content)
        with open(os.path.join(bp,'requirements.txt'), 'wb') as file:
              file.write(dependency)
              print("requirements.txt download completed\n")
              return 1

    dependency=None
    try:
        r = gh_request("/repos/{0}/{1}/contents/package.json".format(username, repo)).json()
    except requests.exceptions.HTTPError:
        print("No package.json found\n")
    else:
        content = r.get("content", None)
        dependency = base64.b64decode(content)
        with open(os.path.join(bp,'package.json'), 'wb') as file:
            file.write(dependency)
            print("package.json download completed\n")
            return 2

def process_repo(repo, clobber=False):
    # Skip forks.
    if repo.get("fork", True):
        return False, False, False
    
    # Get the repository name.
    name = repo["full_name"]

    # Skip if this repo had already been downloaded.
    bp = os.path.join(BASE_DIR, name)
    if not clobber and os.path.exists(bp):
        print(name + " has already been downloaded. Skipping")
        return False, False, False

    print("Processing " + name + " ...")

    # Get the README.
    readme = None
    try:
        r = gh_request("/repos/{0}/readme".format(name)).json()
    except requests.exceptions.HTTPError:
        print("No README found for " + name)
    else:
        content = r.get("content", None)
        if content is not None:
            # Get the repository info.
            try:
                info = gh_request("/repos/{0}".format(name)).json()
            except requests.exceptions.HTTPError:
                print("Can't get info for " + name)
                return False, False, False

            # Save the information.
            try:
                os.makedirs(bp)
            except os.error:
                pass

            with open(os.path.join(bp, "info.json"), "w") as f:
                json.dump(info, f)
                readme = base64.b64decode(content)
                with open(os.path.join(bp, "README.txt"), "wb") as f:
                    f.write(readme)
                arr = extract(os.path.join(bp, "README.txt"))
                installation = ""
                for str in arr:
                    installation = installation + str + '\n'
                if(installation):
                    print("INSTALLATION found for " + name)
                    with open(os.path.join(bp, "INSTALLATION.txt"), "w") as f:
                        f.write(installation)
                else:
                    print("No INSTALLATION found for " + name)
        else:
            print("No README found for " + name)
