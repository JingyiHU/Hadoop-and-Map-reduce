#!/usr/bin/python

import sys
import re

for line in sys.stdin:
  data = line.strip().split(" ")

  if len(data) == 10:
    host,userid,username,datetime,zone,method,queryfile,protocol,state,returnsize = data

    #Split request
    if 'http' in queryfile:
	obj = re.search('^http://.*?(/.*)',queryfile)
	if(obj != None):
    		queryfile = obj.group(1)  
    print queryfile

