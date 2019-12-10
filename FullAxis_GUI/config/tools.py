import pandas as pd
import json
import datetime


def new_user(ID,name,lastname,edad):
	#print(ID,name,lastname,edad)
	date=datetime.datetime.now()
	FC = str(date.day)+'-'+str(date.month)+'-'+str(date.year)
	profile = {	'ID'		:	ID,
				'FC'		: 	FC,
				'nombre'	:	name,
				'lastname'	:	lastname,
				'edad'		:	edad,
				'test'		:	[]
			  }

	with open(str(ID)+'.'+'profile', 'w') as json_file:
				json.dump(profile, json_file)
