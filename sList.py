#!/usr/bin/python
import requests
import json
import uuid
from cache import Cache

class List:
	def __init__(self,server,listId):
		self.listId=listId
		self.server=server
		self.items=[]
		self.title=''
		self.previousSync=None

		self.cache=Cache(self)
		cacheData=self.cache.read()
		if cacheData:
			self.previousSync=cacheData['previousSync']
			currentState=cacheData['currentState']
			self.items=currentState['items']
			self.title=currentState['title']
		self.sync()
	def syncRequestData(self):
		return {
			'previousSync':self.previousSync,
			'currentState':{
				'title':self.title,
				'id':self.listId,
				'items':self.items
			}
		}
	def sync(self):
		if not self.previousSync:
			r=requests.get(self.syncUrl())
		else:
			r=requests.post(self.syncUrl(),json=self.syncRequestData())
		if(r.status_code == 200):
			data=r.json()

			self.previousSync=data
			self.title=str(data.get('title',''))
			self.items=list(data.get('items',''))
		if self.previousSync:
			self.cache.write(self.syncRequestData())

	def syncUrl(self):
		return '{}/api/{}/sync'.format(self.server,self.listId)
	def show(self):
		if self.items:
			print(self.title)
		else:
			print(self.title,'(empty)')
		for item in self.items:
			print("- {}".format(itemStr(item)))
	def add(self,value):
		self.items.append({'stringRepresentation':value, 'id': str(uuid.uuid4())})
		self.sync()
	def delete(self,item):
		self.items.remove(item)
		self.sync()
	def edit(self,item,value):
		if('id' in item):
			itemId=item['id']
			item.clear()
			item['id']=itemId
		else:
			item.clear()
		item['stringRepresentation']=value
		self.sync()
	def clear(self):
		for item in self.items:
			self.delete(item)
		self.sync()

def itemStr(itemDict):
	if 'stringRepresentation' in itemDict:
		return itemDict['stringRepresentation']
	string=itemDict.get('name')
	amount=itemDict.get('amount',None)
	if amount:
		unit=amount.get('unit',None)
		value=amount.get('value',None)
		if unit:
			string='{} {}'.format(unit,string)
		if value:
			string='{} {}'.format(value,string)
	return string
