#!/usr/bin/python

import sys

number = 0
oldpage = None
maxnumber = 0
maxpage = None

for line in sys.stdin:
	thispage = line.strip() 
        
	if oldpage != None and thispage != oldpage:
		print oldpage,": ",number," times click"
		if number > maxnumber:
			maxnumber = number
			maxpage = oldpage 
		oldpage = thispage
		number = 0

	oldpage = thispage
	number = number +1


if oldpage != None:
	print oldpage,": ",number," times click"
	if number > maxnumber:
		maxnumber = number
		maxpage = oldpage 



#Maximum Page
if maxpage != None:
	print "The page most popular is ",maxpage," with a number clik: ",maxnumber
