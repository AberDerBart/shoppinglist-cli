#!/usr/bin/python
import requests
import json

class List:
	def __init__(self,server,listId):
		r=requests.get(server+'/api/'+listId+'/')
		self.listId=listId
		if(r.status_code == 200):
			data=json.loads(r.text)

			self.title=data.get('title','')
			self.title=data.get('title','')
			self.items=[]

			for item in data.get('items',[]):
				self.items.append(Item(item))
	def show(self):
		print(self.title)
		for item in self.items:
			print("- {}".format(str(item)))

class Item:
	def __init__(self,itemDict):
		self.itemDict=itemDict;
	def __str__(self):
		string=self.itemDict.get('name')
		amount=self.itemDict.get('amount',None)
		if amount:
			unit=amount.get('unit',None)
			value=amount.get('value',None)
			if unit:
				string='{} {}'.format(unit,string)
			if value:
				string='{} {}'.format(value,string)
		return string
