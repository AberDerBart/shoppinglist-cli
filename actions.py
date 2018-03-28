from sList import *
from autocomplete import autocomplete
import sys

def addAction(sl,args):
	if(args.value):
		sl.add(args.value)
	else:
		for item in sys.stdin.readlines():
			sl.add(item)
		
	
def delAction(sl,args):
	(item,match)=autocomplete(args.item,sl)
	if(match < .8):
		sys.exit('No matching item found: "{}"'.format(args.item))
	sl.delete(item)

def editAction(sl,args):
	(item,match)=autocomplete(args.item,sl)
	if(match < .8):
		sys.exit('No matching item found: "{}"'.format(args.item))
	sl.edit(item,args.value)

def clearAction(sl,args):
	sl.clear()

actionDict={
	'add': addAction,
	'del': delAction,
	'edit': editAction,
	'clear': clearAction
}
