import Levenshtein

def autocomplete(string,sl):
	bestMatch=None
	value=None

	for item in sl.items:
		tmpValue=Levenshtein.jaro(string.upper(), str(item).upper())
		if not value or tmpValue > value:
			value=tmpValue
			bestMatch=item
	return bestMatch,value
