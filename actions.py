from sList import *

def addAction(sl,args):
	sl.add(args.value)
	
def delAction(sl,args):
	pass

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
