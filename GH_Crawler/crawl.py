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
from repos import get_random_repos, process_repo

while True:
    # Get a list of random repos.
    try:
        repos = get_random_repos()
    except Exception as e:
        print("While getting repos, got exception: ")
        traceback.print_exc()
        continue

    # Loop over these repos and process each one.
    r = []
    for repo in repos:
        try:
            r.append(process_repo(repo))
        except Exception as e:
            print("While analyzing a repo {0}, got exception: ".format(repo["full_name"]))
            traceback.print_exc()
            continue
