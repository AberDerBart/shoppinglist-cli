import argcomplete
import requests
from .cache import Cache
from copy import deepcopy

class ItemStringCompleter(object):
    def __init__(self, config):
        self.config = deepcopy(config)

    def __call__(self, parsed_args, **kwargs):
        server = parsed_args.server or self.config.get('server')
        cachedir = self.config.get('cachedir')
        listId = parsed_args.list or self.config.get('list')

        if not cachedir or not listId or not server:
            return []

        cache = Cache(cachedir, server, listId, '.completion.json')
        data = cache.read() or []

        return data

    def update(config):
        server = config.get('server')
        cachedir = config.get('cachedir')
        listId = config.get('list')

        if not cachedir or not listId or not server:
            return False

        cache = Cache(cachedir, server, listId, '.completion.json')

        r = requests.get('{}/api/{}/completions'.format(server, listId))

        if(r.status_code != 200):
            return False

        tmpData = r.json()
        data = [item['name'] for item in tmpData]
        cache.write(data)
        return True
               
