import Levenshtein
from .sList import itemStr

def matchItem(string,sl):
	bestMatch=None
	value=0

	# extract item by index
	if string.isnumeric():
		item=sl.at(int(string))
		if(item):
			return item,1
		else:
			return item,0

	for item in sl.items:
		tmpValue=Levenshtein.jaro(string.upper(), itemStr(item).upper())
		if not value or tmpValue > value:
			value=tmpValue
			bestMatch=item
	return bestMatch,value
