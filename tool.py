"""tool

Usage:
  tool.py build [ --geo | --info | --visa | --validate ]
  tool.py visa add <cca2> <name> [--default-policy=<visa_type>] [--default-requirement=<visa_type>] [--force]
  tool.py visa set <visa_type> <from-cca2> <to-cca2>... [--cross] [--note=<note>] [--len=<len>]
  tool.py visa rm <cca2> [--force]
  
Options:
  -h --help     Show this screen.
  --version     Show version.

  build
  --geo         Validate and build geo  data
  --info        Validate and build info data
  --visa        Validate and build visa data
  --validate    Validate all data.

  visa
  -p --default-policy=<type>      Sets default visa policy
  -r --default-requirement=<type> Sets default visa requirement
  -f --force                      Force
  --cross                         Cross visa set
  --note=<note>                   Sets note
  --len=<len>                     Sets visa length
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