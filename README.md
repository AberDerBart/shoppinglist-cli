# shoppinglist-cli

a command line client for [shoppinglist](https://github.com/tstehr/shoppinglist)

## Requirements

shoppinglist-cli requires python3 as well as the following python libraries
- requests
- python-Levenshtein
- rcfile
- uuid
## Usage

To use shoppinglist-cli, simply start

```$ python main.py```

## Configuration

For setting a default server and list, place a configuration file like [config.example](config.example) in ~/.shoppinglist-cli/config

Offline caching can be configured using the cachedir parameter in the configuration file.
If the parameter is omitted, no data is cached
