import os
import json
import datetime

class tools:
  def __init__(self):
    pass

  class build:
    def __init__(self, opt):
      if(not opt['--geo'] and not opt['--info'] and 
        not opt['--validate'] and not opt['--visa']):
        print("building")
      else:
        if(opt['--geo']):
          self.geo()
          pass
        elif(opt['--info']):
          self.info()
          pass
        
        elif(opt['--visa']):
          self.visa()
          pass
        elif(opt['--validate']):
          self.validate()
          pass

      print("BUILD SHIT!")
      pass

    def geo(self):
      print("geo")

    def info(self):
      print("info")
      
    def visa(self):
      print("visa")

    def validate(self):
      print("validate")