import requests
from cache import Cache
from config import config

class CategoryList:
	def __init__(self,server,listId):
		self.server=server
		self.listId=listId
		self.categories=None
		if 'cachedir' in config:
			self.cache=Cache(self.server,self.listId,'.cache.json')
			cacheData=self.cache.read()
			if cacheData:
				self.categories=cacheData
		else:
			self.cache=None
	def pull(self):
		r=requests.get('{}/api/{}/categories'.format(self.server,self.listId))
		if(r.status_code == 200):
			data=r.json()
			self.categories={}

			for cat in data:
				catId=cat.get('id')
				if(catId):
					self.categories[catId]=cat
			if self.cache:
				self.cache.write(self.categories)
	
