#!/usr/bin/python

import sys
import csv
import operator


reader = csv.reader(sys.stdin, delimiter='\t', lineterminator='\r\n')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar = '"', quoting = csv.QUOTE_ALL)

rev_tab = dict()
oldnodeid = None

for line in reader:
	if (line != None) and (len(line) == 3):
		node_id, node_type, tagnames = line
	else:
		continue
	
	if node_type == "question":
		wordtab = tagnames.split(" ")
		for word in wordtab:
			if word in rev_tab.keys():
				rev_tab[word] = int(rev_tab[word]) + 1
			else:
				rev_tab[word] = 1


rev_tab = sorted(rev_tab.items(),key=operator.itemgetter(1),reverse=True)

	
Topn = 10
i = 0;
for i in range(0,10):
	writer.writerow(rev_tab[i])
	



	
		



		
