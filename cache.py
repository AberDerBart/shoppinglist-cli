from config import config
import os.path
import json
from sList import * 

class CachedList(List):
	def __init__(self,server,listId,cacheFile):
		super().__init__(server,listId)

		self.cacheFile=cacheFile
