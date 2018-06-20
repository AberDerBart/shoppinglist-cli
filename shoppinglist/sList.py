#!/usr/bin/python
import requests
import json
import uuid
import sys
from .cache import Cache
from .config import config
from .category import CategoryList

class List:
	def __init__(self,server,listId):
		self.listId=listId
		self.server=server
		self.items=[]
		self.title=''
		self.previousSync=None
		self.synced=False
		self.catList=CategoryList(server,listId)

		if 'cachedir' in config:
			self.cache=Cache(self.server,self.listId)
			cacheData=self.cache.read()
			if cacheData:
				self.previousSync=cacheData['previousSync']
				currentState=cacheData['currentState']
				self.items=currentState['items']
				self.title=currentState['title']
			else:
				self.sync()
		else:
			self.cache=None
			self.sync()
		if not self.synced and not self.previousSync:
			sys.exit('List "{}" is not cached and cannot be fetched from server "{}".'.format(self.listId,self.server))
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
		try:
			if not self.previousSync:
				r=requests.get(self.syncUrl())
			else:
				r=requests.post(self.syncUrl(),json=self.syncRequestData())
			if(r.status_code == 200):
				data=r.json()

				self.previousSync=data
				self.title=str(data.get('title',''))
				self.items=list(data.get('items',''))

				self.synced=True
				# server appears to be reachable, pull categories
				self.catList.pull()
		except IOError:
			pass
		if self.cache and self.previousSync:
			self.cache.write(self.syncRequestData())

	def syncUrl(self):
		return '{}/api/{}/sync'.format(self.server,self.listId)
	def show(self):
		attr=[]
		if not self.synced:
			attr.append('offline')
		if not self.items:
			attr.append('empty')
		if attr:
			print(self.title,'({})'.format(', '.join(attr)))
		else:
			print(self.title)
		for item in self.items:
			print("- {}".format(itemStr(item,self.catList)))
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
		self.items.clear()
		self.sync()
	def at(self, index):
		if 0 < index <= len(self.items):
			return self.items[index - 1]
		else:
			return None


def catStr(catId, catList):
	if config.get('categories','').upper()=='SHORT':
		if catId and catList and catList.available():
			category=catList.get(catId)
			if not category:
				return ''
			return '({}) '.format(category.get('shortName','?'))
	return ''

def itemStr(itemDict, catList=None):
	# extract category
	catId=itemDict.get('category')
	category=None
	catString=catStr(catId,catList)

	if 'stringRepresentation' in itemDict:
		return catString + itemDict['stringRepresentation']

	string=itemDict.get('name')
	amount=itemDict.get('amount',None)
	if amount:
		unit=amount.get('unit',None)
		value=amount.get('value',None)
		if unit:
			string='{} {}'.format(unit,string)
		if value:
			string='{} {}'.format(value,string)
	return catString + string
