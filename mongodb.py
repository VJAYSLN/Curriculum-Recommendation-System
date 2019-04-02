# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 19:18:49 2018

@author: VJAY
"""

import http.client
conn = http.client.HTTPConnection("2factor.in")
from pymongo import MongoClient
client=MongoClient('localhost',27017)
db=client.test
collect=db.collect
