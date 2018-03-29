#!/usr/bin/python

import sys

item = 0
salesTotal = 0
oldkey = None

for line in sys.stdin:
	data_mapped = line.strip().split("\t")  
	if len(data_mapped) != 3:
        # Something has gone wrong. Skip this line.
        	continue
	
	
	thiskey,thisitem,thissale = data_mapped

	salesTotal = salesTotal + float(thissale)
	item = item +1


print "Total sale is ",salesTotal
print "Total item number is ",item
	
	
