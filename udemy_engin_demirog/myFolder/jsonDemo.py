# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 15:57:37 2019

@author: EmreKARA
"""

import json

with open("users.json") as users:
    data = json.load(users)
    for i in range(10):
        print(data[i]["address"]["street"])