

"""tool

Usage:
  tool.py build [ --geo | --info | --visa | --validate ]
  tool.py geo add <cc2> <name> [--default-policy=<type>] [--default-requirement=<type>]
Options:
  -h --help     Show this screen.
  --version     Show version.
  -p --default-policy=<type>
  -r --default-requirement=<type>
"""

from docopt import docopt
from tools import tools
      
if __name__ == '__main__':
    arguments = docopt(__doc__, version='tool 0.1')
    # print(arguments)
    if(arguments["build"]):
      tools.build(arguments)