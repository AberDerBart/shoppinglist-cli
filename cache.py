from config import config
import os.path
import json
from sList import * 
from hashlib import md5
import sys

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
		try:
			if not os.path.exists(self.cacheFileDir):
				os.makedirs(self.cacheFileDir)
			with open(self.cacheFileName,'w') as f:
				json.dump(data,f)
		except Exception as e:
			print('Error writing cache file "{}": {}'.format(self.cacheFileName,str(e)),file=sys.stderr)
	def read(self):
		try:
			with open(self.cacheFileName) as f:
				data=json.load(f)
				return data
		except FileNotFoundError:
			return None
		except Exception as e:
			print('Error reading cache file "{}": {}'.format(self.cacheFileName,str(e)),file=sys.stderr)
