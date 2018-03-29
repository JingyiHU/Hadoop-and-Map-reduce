#!/usr/bin/python

import sys

for line in sys.stdin:
  data = line.strip().split(" ")

  if len(data) == 10:
    host,userid,username,datetime,zone,method,queryfile,protocol,state,returnsize = data

    #Split request
    print host

