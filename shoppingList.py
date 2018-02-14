#!/usr/bin/python
import requests
import json

class List:
	def __init__(self,server,listId):
		r=requests.get(server+'/api/'+listId+'/')
		if(r.status_code == 200):
			data=json.loads(r.text)

			self.title=data.get('title','')
			self.title=data.get('title','')
			self.items=[]

			for item in data.get('items',[]):
				self.items.append(Item(item))

class Item:
	def __init__(self,itemDict):
		self.itemDict=itemDict;
	def __str__(self):
		if self.itemDict.get('amount',None):
			return self.itemDict.get('amount')+self.itemDict.get('name')
		return self.itemDict.get('name')
