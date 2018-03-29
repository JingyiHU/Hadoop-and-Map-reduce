#!/usr/bin/python

import sys

number = 0
oldpage = None

for line in sys.stdin:
	thispage = line.strip() 
        
	if oldpage != None and thispage != oldpage:
		print oldpage,": ",number," times click"
		oldpage = thispage
		number = 0

	oldpage = thispage
	number = number +1


if oldpage != None:
	print oldpage,": ",number," times click"
