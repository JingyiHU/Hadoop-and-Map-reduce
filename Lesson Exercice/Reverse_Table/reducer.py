#!/usr/bin/python

import sys

indextable = dict()

for line in sys.stdin:
  data = line.strip().split("\t")

  if len(data) == 2:
  	node_id,bodydata = data
  	
	indexlist = bodydata.strip().split(",")
	
	if node_id not in indextable.keys():
		indextable[node_id] = list()

	indextable[node_id].append(indexlist) 	


for key in indextable.keys():
	indextable[key] = sorted(indextable[key])
	print key,": ",indextable[key]
