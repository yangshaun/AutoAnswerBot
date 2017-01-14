# -*- coding: utf8 -*-
import json
all_answer=[]
with open('questions.json', 'r') as f:
	JsonList = json.load(f)
	for each in JsonList:
		all_answer.append(each['Answer : '].encode('utf8'))
print all_answer
