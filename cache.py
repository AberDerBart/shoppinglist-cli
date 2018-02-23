from config import config
import os.path
import json
from sList import * 

class Cache:
	def __init__(self,listInstance):
		self.listInstance=listInstance	
		self.cacheFileName=os.path.expanduser(config.get('cachedir')+'/'+self.listInstance.listId+'.json')
		self.cacheFileDir= os.path.dirname(self.cacheFileName)
	def write(self,data):
		if not os.path.exists(self.cacheFileDir):
			os.makedirs(self.cacheFileDir)
		f=open(self.cacheFileName,'w')
		json.dump(data,f)
		f.close()
	def read(self):
		f=open(self.cacheFileName)
		if f:
			data=json.load(f)
			f.close()
			return data
		else:
			return None

