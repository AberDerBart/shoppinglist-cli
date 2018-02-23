import Levenshtein
from sList import itemStr

def autocomplete(string,sl):
	bestMatch=None
	value=0

	for item in sl.items:
		tmpValue=Levenshtein.jaro(string.upper(), itemStr(item).upper())
		if not value or tmpValue > value:
			value=tmpValue
			bestMatch=item
	return bestMatch,value
