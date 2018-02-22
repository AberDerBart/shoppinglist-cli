import actions
from sList import List
from config import config,args


sl=List(config.get('server') or DEFAULT_SERVER,config.get('list') or DEFAULT_LIST)

if(args.command):
	actions.actionDict[args.command](sl,args)

sl.show()
