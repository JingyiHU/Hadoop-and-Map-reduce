#!/usr/bin/python

import sys
import csv
import operator


reader = csv.reader(sys.stdin, delimiter='\t', lineterminator='\r\n')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar = '"', quoting = csv.QUOTE_ALL)

forum_dic = dict()

for line in reader:
	if (line != None) and (len(line) == 4):
		node_id, node_type, author_id, parent_id = line
	else:
		continue
	
	if node_type == 'question':
		if node_id not in forum_dic.keys():
			forum_dic[node_id] = list()
		forum_dic[node_id].append(author_id)
	else:
		if parent_id not in forum_dic.keys():
			forum_dic[parent_id] = list()
		forum_dic[parent_id].append(author_id)

for key in forum_dic.keys():
	forum_dic[key] = sorted(forum_dic[key])
	print key,"\t",forum_dic[key]


	



	
		



		
