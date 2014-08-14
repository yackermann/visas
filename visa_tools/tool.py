"""tool

Usage:
  tool.py build geo
  tool.py build info
  tool.py build visa
  tool.py build validate

Options:
  -h --help     Show this screen.
  --version     Show version.

"""

from docopt import docopt
import os
import json
import datetime

if __name__ == '__main__':
    arguments = docopt(__doc__, version='tool 0.1')
    print(arguments)

class tool:
  def __init__(self):
    pass

  class build:
    def __init__(self):
      pass

    def geo():
      pass

    def info():
      pass

    def visa():
      pass

    def validate():
      pass