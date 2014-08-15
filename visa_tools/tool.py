

"""tool

Usage:
  tool.py build [ --geo | --info | --visa | --validate ]
  tool.py visa add <cc2> <name> [--default-policy=<visa_type>] [--default-requirement=<visa_type>]
  tool.py visa set <visa_type> <from-cca2> <to-cca2>... [--cross]
  tool.py visa rm <cca2>
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
    print(arguments)
    if(arguments["build"]):
      tools.builder(arguments)