from sList import *
from autocomplete import autocomplete

def addAction(sl,args):
	sl.add(args.value)
	
def delAction(sl,args):
	(item,match)=autocomplete(args.item,sl)
	if(match < .9):
		raise KeyError('No matching item found: "{}"'.format(args.item))
	sl.delete(item)

def editAction(sl,args):
	(item,match)=autocomplete(args.item,sl)
	if(match < .9):
		raise KeyError('No matching item found: "{}"'.format(args.item))
	sl.edit(item,args.value)

def clearAction(sl,args):
	sl.clear()

actionDict={
	'add': addAction,
	'del': delAction,
	'edit': editAction,
	'clear': clearAction
}
