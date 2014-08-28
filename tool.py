"""tool

Usage:
  tool.py build [ --geo | --info | --visa | --validate ]
  tool.py visa add <cca2> <name> [--default-policy=<visa_type>] [--default-requirement=<visa_type>] [--force]
  tool.py visa set <visa_type> <from-cca2> (--cross | --requirement | --policy) <to-cca2>... [--note=<note>] [--time=<time>]
  tool.py visa rm <cca2> [--force]
  
Options:
  -h --help     Show this screen.
  --version     Show version.
  build
  --geo         Validate and build geo  data
  --info        Validate and build info data
  --visa        Validate and build visa data
  --validate    Validate all data
  visa
  -defp --default-policy=<type>      Sets default visa policy         [default: r] r - required
  -defr --default-requirement=<type> Sets default visa requirement    [default: r] r - required
  -f --force                      Force
  -x --cross                      Cross visa set between this countries
  -r --requirement                Sets requirement for the countrie to the countrie(s)
  -p --policy                     Sets policy of the countrie to the countrie(s)
  --note=<note>                   Sets note        [default: None]
  --time=<time>                   Sets visa length [default: None]
"""

from libs.docopt import docopt
from libs.tools import tools
      
if __name__ == '__main__':
    arguments = docopt(__doc__, version='tool 0.4')
    # print(arguments) #DEBUG
    if(arguments['build']):
      tools.builder(arguments)
    elif(arguments['visa']):
      tools.visa(arguments)