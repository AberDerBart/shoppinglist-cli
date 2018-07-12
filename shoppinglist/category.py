import requests
from distutils.util import strtobool
from tinycss2.color3 import parse_color
from xtermcolor import colorize
from .cache import Cache
from .config import config

class CategoryList:
	def __init__(self,server,listId):
		self.server=server
		self.listId=listId
		self.categories=None
		if 'cachedir' in config:
			self.cache=Cache(self.server,self.listId,'.cat.json')
			cacheData=self.cache.read()
			if cacheData:
				self.categories=cacheData
		else:
			self.cache=None
	def get(self,catId):
		if self.categories:
			return self.categories.get(catId)
		return None
	def available(self):
		return not (self.categories is None)
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
	def show(self):
		for cat in self.categories.values():
			catStr = '({}) {}'.format(cat.get('shortName','?'),cat.get('name'))
			color = catColorAsRGBInt(cat)
			if strtobool(config.get('colored','1')) and color is not None:
				catStr = colorize(catStr, rgb=color)
			print(catStr)

def catColorAsRGBInt(category):
	if 'color' in category:
		rgb = parse_color(category['color'])
		return (int(rgb.red * 255) << 16) + (int(rgb.green * 255) << 8) + int(rgb.blue * 255)
	return None