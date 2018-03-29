#!/usr/bin/python

import sys
import csv


reader = csv.reader(sys.stdin, delimiter='\t', lineterminator='\r\n')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar = '"', quoting = csv.QUOTE_ALL)

ques_dic = dict()
answ_dic = dict()
oldnodeid = None

for line in reader:
	if (line != None) and (len(line) == 4):
		thisnodeid, node_type, parent_id, bodylength = line
	else:
		continue
	
	
	if node_type == 'question':
		if thisnodeid not in ques_dic: 
			ques_dic[thisnodeid] = float(bodylength)
	elif node_type == 'answer':
		if parent_id not in answ_dic:
			answ_dic[parent_id] = list()
		answ_dic[parent_id].append(float(bodylength))

for key in ques_dic.keys():
	if key in answ_dic:
		print key,"\t",ques_dic[key],"\t",sum(answ_dic[key])/len(answ_dic[key])
	else:
		print key,"\t",ques_dic[key],"\t","No Answers"


	
		



		
