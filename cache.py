from config import config
import os.path
import json
from sList import * 
from hashlib import md5

def cleanString(string):
	'''transforms given string into something you can use as filename'''
	cleaned=''.join(c for c in string if (c.isalnum() or c in '._'))
	hashStr=md5(string.encode()).hexdigest()
	return cleaned+'_'+hashStr

class Cache:
	def __init__(self,listInstance):
		self.listInstance=listInstance	
		self.cacheFileName=os.path.expanduser('{}/{}/{}.json'.format(
			config.get('cachedir'),
			cleanString(self.listInstance.server),
			cleanString(self.listInstance.listId)
		))
		self.cacheFileDir= os.path.dirname(self.cacheFileName)
	def write(self,data):
		if not os.path.exists(self.cacheFileDir):
			os.makedirs(self.cacheFileDir)
		f=open(self.cacheFileName,'w')
		json.dump(data,f)
		f.close()
	def read(self):
		try:
			with open(self.cacheFileName) as f:
				data=json.load(f)
				return data
		except FileNotFoundError:
			return None
