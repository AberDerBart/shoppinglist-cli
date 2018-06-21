import Levenshtein
from .sList import itemStr

def matchItem(string,sl):
	bestMatch=None
	value=0

	# extract item by index
	if string.isnumeric():
		return sl.at(int(string)),1

	for item in sl.items:
		tmpValue=Levenshtein.jaro(string.upper(), itemStr(item).upper())
		if not value or tmpValue > value:
			value=tmpValue
			bestMatch=item
	return bestMatch,value
