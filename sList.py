#!/usr/bin/python
import requests
import json

class List:
	def __init__(self,server,listId):
		self.listId=listId
		self.server=server
		self.load()
	def load(self):
		r=requests.get(self.listUrl())
		if(r.status_code == 200):
			data=json.loads(r.text)

			self.title=data.get('title','')
			self.title=data.get('title','')
			self.items=[]

			for item in data.get('items',[]):
				self.items.append(Item(item))
	def listUrl(self):
		return '{}/api/{}'.format(self.server,self.listId)
	def show(self):
		print(self.title)
		for item in self.items:
			print("- {}".format(str(item)))
	def add(self,value):
		r=requests.post(self.listUrl()+'/items?parse',json=value)
		self.load()
	def delete(self,item):
		r=requests.delete(self.listUrl()+'/items/'+item.id())
		self.load()
	def edit(self,item,value):
		r=requests.put(self.listUrl()+'/items/{}?parse'.format(item.id()),json=value)

		self.load()

class Item:
	def __init__(self,itemDict):
		self.itemDict=itemDict;
	def id(self):
		return self.itemDict.get('id')
	def name(self):
		return self.itemDict.get('name')
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
