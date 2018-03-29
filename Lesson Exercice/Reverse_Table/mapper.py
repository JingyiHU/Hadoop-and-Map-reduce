#!/usr/bin/python

import sys

def wordformer(word):
	if word != None:
		word = word.replace('\"','')
		word = word.replace('<p>','')
		word = word.replace('</p>','')
		word = word.replace('[0-9]*','')	
		word = word.replace("%","")
		word = word.replace("?","")
		word = word.replace(",","")
		word = word.replace("'","")
		#print word

	return word
		
dic = dict()

for line in sys.stdin:
  data = line.strip().split("\t")

  if len(data) == 19:
  	nodeid,title,tagnames,author_id,body,node_type,parent_id,abs_parent_id,added_at,score,state_string,last_edited_id,last_activity_by_id,last_activity_at,active_revision_id,extra,extra_ref_id,extra_count,marked = data
	bodydata = body.strip().split(" ")
	nodeid = nodeid.replace("\"","")
	for word in bodydata:
		word = wordformer(word)
		word = word.lower()
		
		if word != "":
			if word not in dic.keys():
				dic[word] = list()
			dic[word].append(nodeid)	

for key in dic.keys():
	dic[key] = sorted(dic[key])
	print key,"\t",dic[key]	
	
