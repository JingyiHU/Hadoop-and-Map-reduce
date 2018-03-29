#!/usr/bin/python

import sys

maxSale = 0
oldkey = None
oldsale = 0
count = 0

for line in sys.stdin:
	data_mapped = line.strip().split("\t")  
	
	if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        	continue
	

	thiskey,thissale = data_mapped


	if oldkey == None:
		oldkey = thiskey
		maxSale = float(thissale)
	else:
		if oldkey == thiskey:
			count = count +1
			if float(maxSale) < float(thissale):
				maxSale = float(thissale)
		else:
			if count == 0:
				print "The shop is ",oldkey, "The max sale is ",oldsale
			else:
				print "The shop is ",oldkey, "The max sale is ",maxSale
			
			oldkey = thiskey
			oldsale = thissale
			maxSale = 0
			count = 0

if oldkey != None:
	print "The shop is ",oldkey, "The max sale is ",thissale



