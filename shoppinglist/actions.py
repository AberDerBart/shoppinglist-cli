from .sList import *
from .match import matchItem
import sys

def categoriesAction(sl,args):
	sl.catList.show()

def addAction(sl,args):
	if(args.value):
		sl.add(' '.join(args.value))
	else:
		for item in sys.stdin.readlines():
			if not item.isspace():
				sl.add(item)
	sl.show()
		
	
def delAction(sl,args):
	item, match = matchItem(args.item,sl)
	if(match < .8):
		sys.exit('No matching item found: "{}"'.format(args.item))
	sl.delete(item)
	sl.show()

def editAction(sl,args):
	item, match = matchItem(args.item,sl)
	if(match < .8):
		sys.exit('No matching item found: "{}"'.format(args.item))
	sl.edit(item,' '.join(args.value))
	sl.show()

def clearAction(sl,args):
	sl.clear()
	sl.show()

actionDict={
	'add': addAction,
	'del': delAction,
	'edit': editAction,
	'clear': clearAction,
	'categories': categoriesAction
}
