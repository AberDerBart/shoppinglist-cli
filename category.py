import requests

class Category:
	def __init__(self,catDict):
		self.id=catDict.get('id')
		self.name=catDict.get('name')
		self.shortName=catDict.get('shortName')
		self.color=catDict.get('color')
		self.lightText=catDict.get('lightText')

class CategoryList:
	def __init__(self,server,listId):
		self.server=server
		self.listId=listId
	def pull(self):
		r=requests.get('{}/api/{}/categories'.format(self.server,self.listId))
		if(r.status_code == 200):
			print(r.text)
			data=r.json()
			self.categories={}

			for cat in data:
				catId=cat.get('id')
				if(catId):
					self.categories[catId]=Category(cat)
	
