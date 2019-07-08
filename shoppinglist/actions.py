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
	sl.sync()
	sl.show()
		
	
def delAction(sl,args):
	itemsToDelete=[]
	for itemStr in args.items.split(','):
		item, match = matchItem(itemStr,sl)
		if(match < .8):
			sys.exit('No matching item found: "{}"'.format(itemStr))
		itemsToDelete = itemsToDelete + [item]
	for item in itemsToDelete:
		sl.delete(item)
	sl.sync()
	sl.show()

def editAction(sl,args):
	item, match = matchItem(args.item,sl)
	if(match < .8):
		sys.exit('No matching item found: "{}"'.format(args.item))
	sl.edit(item,' '.join(args.value))
	sl.sync()
	sl.show()

def clearAction(sl,args):
	sl.clear()
	sl.sync()
	sl.show()

actionDict={
	'add': addAction,
	'del': delAction,
	'edit': editAction,
	'clear': clearAction,
	'categories': categoriesAction
}
