import argparse
import actions
from sList import List
import os

server='https://list.tilman.ninja'
listId='Demo'

if 'SHOPPINGLIST_ID' in os.environ:
	listId=os.environ['SHOPPINGLIST_ID']
if 'SHOPPINGLIST_SERVER' in os.environ:
	server=os.environ['SHOPPINGLIST_SERVER']

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

parser.add_argument("--list",help="sets the list ID",default=listId)
parser.add_argument("--server",help="the URL of the server to contact",default=server)

args=parser.parse_args()

sl=List(args.server,args.list)

if(args.command):
	actions.actionDict[args.command](sl,args)

sl.show()
