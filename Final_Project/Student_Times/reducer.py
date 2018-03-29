#!/usr/bin/python

import sys
import csv

def getbesthour(hours):
	besthour = list()
	maxcount = 0
	for i in range(1,24):
		if(hours[i] > maxcount):
			maxcount = hours[i]

	for i in range(1,24):
		if(hours[i] == maxcount):
			besthour.append(i)

	return besthour

reader = csv.reader(sys.stdin, delimiter='\t', lineterminator='\r\n')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar = '"', quoting = csv.QUOTE_ALL)
hours = [0]*25
besthour = None
olduserid = None

for line in reader:
	if (line != None) and (len(line) == 2):
		thisuserid,hour = line
		hour = int(hour)
	else:
		continue
	
	if (olduserid != None) and (olduserid != thisuserid):
		besthour = getbesthour(hours)
		for bh in besthour:
			new_data = [olduserid,bh] 
			writer.writerow(new_data)
		besthour = None		
		hours = [0]*25	

	olduserid = thisuserid
	hours[hour] = hours[hour]+1	

if(olduserid != None):
	besthour = getbesthour(hours)
	for bh in besthour:
		new_data = [olduserid,bh] 
		writer.writerow(new_data)
		



		
