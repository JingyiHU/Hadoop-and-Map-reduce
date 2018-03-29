#!/usr/bin/python

import sys

number = 0
oldhost = None

for line in sys.stdin:
	thishost = line.strip() 
        
	if oldhost != None and thishost != oldhost:
		print oldhost,": ",number," times click"
		oldhost = thishost
		number = 0

	oldhost = thishost
	number = number +1


if oldhost != None:
	print oldhost,": ",number," times click"
