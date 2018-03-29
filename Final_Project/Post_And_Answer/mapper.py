#!/usr/bin/python

import sys
import csv



reader = csv.reader(sys.stdin, delimiter='\t', lineterminator='\r\n')
next(reader,None)
writer = csv.writer(sys.stdout, delimiter='\t', quotechar = '"', quoting = csv.QUOTE_ALL)


for line in reader:
	if (line != None) and (len(line) == 19):
		node_id, title, tagnames, author_id, body, node_type, parent_id, abs_parent_id, added_at, score, state_string, last_edited_id, last_activity_by_id, last_activity_at, active_version_id, extra, extra_ref_id, extra_count, marked = line 
		hour = (added_at.strip().split(" ",1)[-1]).split(":")[0]
		bodylength = len(body)
		new_data = [node_id,node_type,parent_id,bodylength]
	
		writer.writerow(new_data)
		
	
