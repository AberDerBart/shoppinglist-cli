import actions
from sList import List
from config import config,args


sl=List(config.get('server'),config.get('list'))

if(args.command):
	actions.actionDict[args.command](sl,args)

sl.show()
