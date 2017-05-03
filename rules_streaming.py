#!/usr/bin/python

import json
import datetime
from datetime import *


f=open("dump.json","r")
data=json.loads(f.read())

def rules(data): #Rule Function
	for i in range(len(data)):
		val=data[i]['value_type']
		if val=="String":             		#Rule 1 if string value is not HIGH
			if data[i]['value']=='LOW':
				with open("final_data.txt","a") as fd:
					json.dump(data[i],fd)
		elif val=="Integer": 
			if float(data[i]['value'])>240:		#Rule 2 if Integer value is greater than 240
				with open("final_data.txt","a") as integer:
					json.dump(data[i],integer)
		elif val=="Datetime":
			old_date=datetime.strptime(data[i]['value'],"%Y-%m-%d %H:%M:%S")  #Rule 3 if future date is present
			now=datetime.now()
			if old_date>now:
				with open("final_data.txt","a") as dt:
					json.dump(data[i],dt)


if __name__=="__main__":
	rules(data)
