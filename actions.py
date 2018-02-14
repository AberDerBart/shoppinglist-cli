from sList import *
from autocomplete import autocomplete

def addAction(sl,args):
	sl.add(args.value)
	
def delAction(sl,args):
	(item,match)=autocomplete(args.item,sl)
	sl.delete(item)

def editAction(sl,args):
	(item,match)=autocomplete(args.item,sl)
	sl.edit(item,args.value)
	pass

def clearAction(sl,args):
	sl.clear()

actionDict={
	'add': addAction,
	'del': delAction,
	'edit': editAction,
	'clear': clearAction
}
