import argcomplete
import requests
from .config import config
from .cache import Cache

class ItemStringCompleter(object):
    def __init__(self, server, listId):
        self.server = server
        self.listId = listId
        self.items = []
        self.completions = []
        self.cache = None

        if('cachedir') in config:
            self.cache = Cache(server, listId, '.completions.json')
            self.completions = self.cache.read() or []

    def pull(self):
        r = requests.get('{}/api/{}/completions'.format(self.server, self.listId))
        if(r.status_code == 200):
            self.completions = r.json()
            if self.cache:
                self.cache.write(self.completions)
    def getList(self):
        return [item.get('name') for item in self.completions]

