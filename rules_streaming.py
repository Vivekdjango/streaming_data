#!/usr/bin/python
__author__="Vivek"
import json
import datetime
from datetime import *
from ConfigParser import SafeConfigParser
import re
import ConfigParser 
parser = SafeConfigParser()
parser.read('rules.ini')

config=ConfigParser.ConfigParser()

json_data=open("data.json","r")
d=json.loads(json_data.read())

def update_rules():
	cnf=raw_input("Would you like to update rules: [yes/no]:")
	if cnf == "no":
		return "No update"
	else:
		i1=raw_input("Enter id value:")
		i2=raw_input("Enter value type:")
		if i2=="String":
			c1=raw_input("Enter Violate Condition: [HIGH/LOW]")
		if i2=="Integer":
			c1=raw_input("Enter numeric value and Condition: [val,gt/lt/eq]")
		if i2=="Datetime":
			c1=raw_input("Enter Condition: [past/future]")

		f=open("rules.ini","a+")
	        config.read("rules.ini")
		d=config.sections()
		if len(d)==0:
			r1="Rule1"	
			config.add_section(r1)
			num=re.findall("\d+",i1)
			config.set(r1,"id",num)
			config.set(r1,"value_type",i2)
			config.set(r1,"condition",c1)
			config.write(f)
			f.close()
		else:
			r1="Rule%d"%(int(re.findall('\d+',parser.sections()[-1])[0])+1)
			f.write("\n")
			config.add_section(r1)
                        num=re.findall("\d+",i1)
                        config.set(r1,"id",num)
                        config.set(r1,"value_type",i2)
                        config.set(r1,"condition",c1)
                        config.write(f)
                    	f.close()
		return "Rules Updated Successfully"


def rules(d): #Rule Function
	for i in range(len(d)):
		rl=open("rules.ini")
		config.read("rules.ini")
		kt=config.sections()
		for it in kt:
			if (parser.get(it,'id')[2]) == (d[i].values()[0].split('L')[1]) and parser.get(it,'value_type')==d[i]['value_type']:
				if parser.get(it,'value_type')=="String":
					if d[i]['value']==parser.get(it,'condition'):
						with open("new_data.txt","a") as fd:
							json.dump(d[i],fd)
				if parser.get(it,'value_type')=="Integer":
					cond=parser.get(it,'condition').split(',')
					if cond[1]=='lt':
						if float(d[i]['value'])<float(cond[0]):
							with open("new_data.txt","a") as fd:
                                                        	json.dump(d[i],fd)
					if cond[1]=='gt':
                                		if float(d[i]['value'])>float(cond[0]):
                                        		with open("new_data.txt","a") as fd:
                                                		json.dump(d[i],fd)
					if cond[1]=='eq':
                                		if float(d[i]['value'])==float(cond[0]):
                                        		with open("new_data.txt","a") as fd:
                                                		json.dump(d[i],fd)
				
				if parser.get(it,'value_type')=="Datetime":			
					old_date=datetime.strptime(d[i]['value'],"%Y-%m-%d %H:%M:%S")
					now=datetime.now()                                                                 
					if parser.get(it,'condition')=="past":
						if old_date<now:
							with open("new_data.txt","a") as dt:
								json.dump(d[i],dt)
					
					if parser.get(it,'condition')=="future":
						if old_date>now:
							with open("new_data.txt","a") as dt:
                                                		json.dump(d[i],dt)


if __name__=="__main__":
	if update_rules()=="Updated":
		print "Updated"
	else:
		rules(d)
