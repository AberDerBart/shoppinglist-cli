from sList import *
from autocomplete import autocomplete

def addAction(sl,args):
	sl.add(args.value)
	
def delAction(sl,args):
	(item,match)=autocomplete(args.item,sl)
	print('del',str(item),item.itemDict.get('id'))
	if not sl.delete(item):
		print('ERROR')


def editAction(sl,args):
	pass

def clearAction(sl,args):
	pass

actionDict={
	'add': addAction,
	'del': delAction,
	'edit': editAction,
	'clear': clearAction
}
