# shoppinglist-cli

a command line client for [shoppinglist](https://github.com/tstehr/shoppinglist)

## Requirements

shoppinglist-cli requires python3 as well as the following python libraries
- requests
- python-Levenshtein
- rcfile
- uuid

## Installation

To install shoppinglist-cli, run

```$ python setup.py install```

## Usage

Display the list:

```$ shoppinglist```

Display the list _Brian_:

```$ shoppinglist --list Brian```

Add _spam_ to the list:

```$ shoppinglist add spam```

Change _spam_ to _eggs_:

```$ shoppinglist edit Spam eggs```

Delete _eggs_:

```$ shoppinglist del eggs```

Delete the third item:

```$ shoppinglist del 3```

For further usage information, run:

``` $ shoppinglist [command] --help```

## Configuration

For setting a default server and list, place a configuration file like [config.example](config.example) in ~/.shoppinglist-cli/config

Offline caching can be configured using the cachedir parameter in the configuration file.
If the parameter is omitted, no data is cached
