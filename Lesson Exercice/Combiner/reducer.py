#!/usr/bin/python

import sys

salesTotal = 0
items = 0
oldkey = None

sumbyweek = dict()

for line in sys.stdin:
	data_mapped = line.strip().split("\t")  
	if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        	continue
	

	thiskey,thissale = data_mapped

	if thiskey not in sumbyweek.keys():
		sumbyweek[thiskey] = 0

	sumbyweek[thiskey] = sumbyweek[thiskey] + float(thissale)


for key in sumbyweek.keys():
	print "{0}\t{1}".format(key, sumbyweek[key])	
	
	
