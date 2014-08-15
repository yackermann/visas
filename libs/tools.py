import os
import json
import datetime

class tools:
  def __init__(self):
    pass

  class builder:
    def __init__(self, opt):
      if(not opt['--geo'] and not opt['--info'] and 
        not opt['--validate'] and not opt['--visa']):
        if not self.validate():
          self.build()
        else: print('\nError while build. Some files have failed validating.')
      else:
        if(opt['--geo']): 
          if not self.validate('geo'): 
            self.build('geo') 
          else: print('\nError while build. Some files have failed validating.')

        elif(opt['--visa']):
          if not self.validate('visa'): 
            self.build('visa') 
          else: print('\nError while build. Some files have failed validating.')

        elif(opt['--info']): 
          self.build('info')

        elif(opt['--validate']): 
          self.validate()

    def build(self, chosen=None):
      data = {}
      builds = 'dist'
      folders = [chosen] if chosen else ['visa','geo', 'info']
      for i in folders:
        data[i] = []
        folder = 'data/' + i
        print('Building ' + i + '...')
        for file in os.listdir(folder):
          if file.endswith('.json'):
            with open(folder + '/' + file) as f:
              if(i == 'geo'):
                data[i] = {'type' : 'FeatureCollection','features': []}
                data[i]['features'].append(json.loads(f.read())['features'][0])
              elif(i == 'info'):
                data[i] = json.loads(f.read())
              else:
                data[i].append(json.loads(f.read()))

      for i in data:
        file = 'world.' + i + '.json'
        with open(builds + '/' + file, 'w') as w:
          w.write(json.dumps(data[i]))
        print('Building ' + i + ' complete.')

      if not chosen:
        self.todo(data)



    def validate(self, chosen=None):
      b = '=========================='
      er = False
      folders = [chosen] if chosen else ['visa','geo']
      for i in folders:
        folder = 'data/' + i
        print(b + '\nStarting to validate ' + i + '\n')
        for file in os.listdir(folder):
          if file.endswith('.json'):
            try:
              data = ''
              with open(folder + '/' + file) as f:
                data = json.loads(f.read())

              with open(folder + '/' + file, 'w') as w:
                w.write(json.dumps(data, sort_keys=True, indent=4, separators=(',', ': ')))
            except:
              er = True
              print('Error while validating file: ' + folder + '/' + file)
        print('\nValidation of ' + i + ' data completed.\n' + b)
      return er

    def todo(self, data):
      todo_str = ''
      tododata = {
        'geo' : [],
        'visa': []
      }
      print('Generating todo...')
      for i in data['visa']:
        tododata['visa'].append(i['cca2'])

      for i in data['geo']['features']:
        tododata['geo'].append(i['id'])

      for i in tododata:
        todo_str += '### Todo for ' + i + ' data\n'
        for n in data['info']:
          if n['cca2'] not in tododata[i]:
            todo_str += '- ' + n['cca2'] + '\t:\t' + n['name'] + '\n'
      with open('TODO.md','w') as w:
        w.write(todo_str)
      print('Generating todo complete.')