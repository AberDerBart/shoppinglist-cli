import argparse
import rcfile


DEFAULT_SERVER = 'https://list.tilman.ninja'
DEFAULT_LIST = 'Demo'

# setup cli parser
parser=argparse.ArgumentParser()
subParsers=parser.add_subparsers(dest="command")
subParsers.required=False

addParser=subParsers.add_parser("add",help="adds an item to the list")
addParser.add_argument("value",help="the value for item to be added to the list")

delParse=subParsers.add_parser("del",help="deletes an item from the list")
delParse.add_argument("item",help="the item to be deleted from the list")

editParse=subParsers.add_parser("edit",help="edits an item on the list")
editParse.add_argument("item",help="the item to be edited")
editParse.add_argument("value",help="the new value for the item")

clearParse=subParsers.add_parser("clear",help="clears the list")

parser.add_argument("--list",help="sets the list ID")
parser.add_argument("--server",help="the URL of the server to contact")

args=parser.parse_args()

# config from cli args 
argsDict=args.__dict__

# config from evironment
envDict=rcfile.get_environment('shoppingList')

# config from config file
configDict=rcfile.get_config('shoppingList','shoppingList','~/.shoppingList/config')


# merge config with priority cli > environment > config file
config={}
for conf in [configDict,envDict,argsDict]:
	config=rcfile.merge(conf,config)

# set default values if none set
if not config.get('server'):
	config['server'] = DEFAULT_SERVER
if not config.get('list'):
	config['list'] = DEFAULT_LIST
