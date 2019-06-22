import argparse
import rcfile

DEFAULT_SERVER = 'https://list.tilman.ninja'
DEFAULT_LIST   = 'Demo'

parser=argparse.ArgumentParser()
subParsers=parser.add_subparsers(dest="command")
subParsers.required=False

addParser=subParsers.add_parser("add",help="adds an item to the list")
addParser.add_argument("value",help="the value for item to be added to the list",nargs="*",default=None)

delParse=subParsers.add_parser("del",help="deletes an item from the list")
delParse.add_argument("items",help="a comma-seperated list of the items to be deleted from the list or their indices")

editParse=subParsers.add_parser("edit",help="edits an item on the list")
editParse.add_argument("item",help="the item to be edited or its index")
editParse.add_argument("value",help="the new value for the item",nargs="+")

clearParse=subParsers.add_parser("clear",help="clears the list")

categoriesParse=subParsers.add_parser("categories",help="lists the categories")

parser.add_argument("--list",help="sets the list ID")
parser.add_argument("--server",help="the URL of the server to contact")
parser.add_argument("--username",help="Username to send to server")

parser.add_argument("-N","--numbers",help="show list index of items",action="store_const",dest="numbered",const="1")
parser.add_argument("-n","--nonumbers",help="do not show list index of items",action="store_const",dest="numbered",const="0")

parser.add_argument("-C","--color",help="enable colors",dest="colored",action="store_const",const="1")
parser.add_argument("-c","--nocolor",help="disable colors",dest="colored",action="store_const",const="0")


args=parser.parse_args()

cmdArgs={k:v for k,v in args.__dict__.items() if v is not None}

config=rcfile.rcfile('shoppinglist-cli',cmdArgs)

if not config.get('server'):
	config['server']=DEFAULT_SERVER
if not config.get('list'):
	config['list']=DEFAULT_LIST
