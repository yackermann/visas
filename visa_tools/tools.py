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
        if(opt['--geo']): self.geo()
        elif(opt['--info']): self.info()
        elif(opt['--visa']): self.visa()
        elif(opt['--validate']): self.validate()

    def geo(self):
      print("geo")

    def info(self):
      print("info")
      
    def visa(self):
      print("visa")

    def validate(self):
      for i in ['visa','geo']:
        folder = 'data/' + i
        print("Starting to validate " + i)
        for file in os.listdir(folder):
          if file.endswith(".json"):
            try:
              data = ""
              with open(folder + "/"+ file) as f:
                data = json.loads(f.read())

              with open(folder + "/"+ file, "w") as w:
                w.write(json.dumps(data, sort_keys=True, indent=4, separators=(',', ': ')))
            except:
              print("Error while validating file: " + folder + "/" + file)
        print("Validation of " + i + " data completed.")