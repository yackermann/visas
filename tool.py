"""tool

Usage:
  tool.py build [ --geo | --info | --visa | --validate ]
  tool.py visa add <cca2> <name> [--default-policy=<visa_type>] [--default-requirement=<visa_type>] [--force]
  tool.py visa set <visa_type> <from-cca2> <to-cca2>... [--cross] [--note=<note>] [--len=<len>]
  tool.py visa rm <cca2>
Options:
  -h --help     Show this screen.
  --version     Show version.
  --geo         Validate and build geo  data
  --info        Validate and build info data
  --visa        Validate and build visa data
  --validate    Validate all data.
  -p --default-policy=<type>
  -r --default-requirement=<type>

"""

from libs.docopt import docopt
from libs.tools import tools
      
if __name__ == '__main__':
    arguments = docopt(__doc__, version='tool 0.3')
    # print(arguments) #DEBUG
    if(arguments['build']):
      tools.builder(arguments)
    elif(arguments['visa']):
      tools.visa(arguments)