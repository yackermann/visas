"""tool

Usage:
  tool.py build [ --geo | --info | --visa | --validate ]

Options:
  -h --help     Show this screen.
  --version     Show version.
  --geo         Validate and build geo  data
  --info        Validate and build info data
  --visa        Validate and build visa data
  --validate    Validate all data.

"""

from libs.docopt import docopt
from libs.tools import tools
      
if __name__ == '__main__':
    arguments = docopt(__doc__, version='tool 0.3')
    # print(arguments) #DEBUG
    if(arguments["build"]):
      tools.builder(arguments)