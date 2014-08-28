import os
import json
import datetime

class tools:
  def __init__(self):
    pass

  class builder:
    def __init__(self, opt={}):
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
      folders = [chosen] if chosen else ['visa', 'geo', 'info']
      for i in folders:
        data[i] = [] if i != 'geo' else {'type' : 'FeatureCollection','features': []}
        folder = 'data/' + i
        print('Building ' + i + '...')
        for file in os.listdir(folder):
          if file.endswith('.json'):
            with open(folder + '/' + file) as f:
              if(i == 'geo'):
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

  class visa:
    def __init__(self, opt):
      self.__options = opt
      if(opt['add']):
        self.add()
      elif(opt['set']):
        self.set()
      elif(opt['rm']):
        self.rm()

    def add(self):
      defaults = {
        'p': self.__options['--default-policy'],
        'r': self.__options['--default-requirement'],
        'force': self.__options['--force']
      }

      data = {}
      cca2 = self.__options['<cca2>'].upper()
      data[cca2] = {'cca2': cca2,'cca3': '','ccn3': '','name': self.__options['<name>'],'rank': 0,'requirements': {}}

      root = 'data/visa' 
      item = root + '/' + cca2 + '.visa.json'
      try:
        # print(file)
        if not defaults['force']:
          with open(item) as r:
            print('Error. ' + cca2 + ' : ' + data[cca2]['name'] + ' already exists.')
        else:
          raise OSError
      except (OSError, IOError) as e:
        print('Creating ' + data[cca2]['name'] + '...')
        if not tools.builder.validate('', 'visa'):
          keys = []
          for file in os.listdir(root):
            if file.endswith('.visa.json'):
              with open(root + '/' + file) as f:
                item = json.loads(f.read())
                data[item['cca2']] = item

          keys = list(data.keys())
          for i in data:
            if i != cca2:
              data[i]['requirements'][cca2] = {
                'note': '',
                'time': '',
                'type': defaults['p'] if defaults['p'] else 'r'
              }
            else:
              for k in keys:
                if k != cca2:
                  data[cca2]['requirements'][k] = {
                    'note': '',
                    'time': '',
                    'type': defaults['r'] if defaults['r'] else 'r'
                  }

            with open(root + '/' + i + '.visa.json', 'w') as w:
              w.write(json.dumps(data[i], sort_keys=True, indent=4, separators=(',', ': ')))
              print('Done ' + data[i]['name'])
          print('Successfully added ' + data[cca2]['name'] + '.')
        else:
          print('\nError while adding. Some files have failed validating.')

    def set(self):
      defaults = {
        'from'        : self.__options['<from-cca2>'].upper(),
        'to'          : list(set(ccn2.upper() for ccn2 in self.__options['<to-cca2>'])),

        'cross'       : self.__options['--cross'],
        'policy'      : self.__options['--policy'],
        'requirement' : self.__options['--requirement'],

        'type'        : self.__options['<visa_type>'],
        'time'        : self.__options['--time'],
        'note'        : self.__options['--note']
      }
      template = {
              'note': defaults['note'] if defaults['note'] else '',
              'time': defaults['time'] if defaults['time'] else '',
              'type': defaults['type']
      }
      data = {}
      root = 'data/visa'

      def keyser():
        keys = []
        if defaults['requirement']:
          keys = [defaults['from']]
        else:
          keys = defaults['to']
          if defaults['cross']: keys.append(defaults['from'])
        return keys

      keys = keyser()
      def checker(tocheck):
        allgood = True
        for key in tocheck:
          try:
            item = root + '/' + key + '.visa.json'
            with open(item) as r:
              data[key] = json.loads(r.read())
          except (OSError, IOError) as e:
            allgood = False
            print('Failed to load ' + key + '.visa.json')
        return allgood

      def msg(k):
        vpc = ''
        if defaults['requirement']: vpc = 'set visa requirement for ' +  defaults['from'] + ' to ' + k
        elif defaults['policy']: vpc = 'set visa policy of ' +  defaults['from'] + ' to ' + k
        else: vpc = 'done ' + k
        print('Successfully ' + vpc)

      if checker(keys):
        if defaults['requirement']:   #Requirement
          for key in defaults['to']:
            data[keys[0]]['requirements'][key] = template
            msg(key)

        elif defaults['policy']:      #Policy
          for key in keys:
            data[key]['requirements'][defaults['from']] = template
            msg(key)

        else:                         #Cross
          for key in keys:
            for k in keys:
              if k != key:
                data[key]['requirements'][k] = template
                msg(key)

        for key in keys:
          item = root + '/' + key + '.visa.json'
          with open(item, 'w') as w:
            w.write(json.dumps(data[key], sort_keys=True, indent=4, separators=(',', ': ')))
      else:
        print('Some files are missing. Please check your input again.')


    def rm(self):
      defaults = {'cca2':self.__options['<cca2>'],'force':self.__options['--force']}
      root = 'data/visa' 
      item = root + '/' + defaults['cca2'] + '.visa.json'
      data = []
      if os.path.isfile(item) or defaults['force']:
        print('Removing ' + defaults['cca2'])
        if os.path.isfile(item): os.remove(item)
        for file in os.listdir(root):
          if file.endswith('.visa.json'):
            with open(root + '/' + file) as f:
              temp = json.loads(f.read())
              temp['requirements'].pop(defaults['cca2'], None)
              with open(root + '/' + file, 'w') as w:
                w.write(json.dumps(temp, sort_keys=True, indent=4, separators=(',', ': ')))
              print(defaults['cca2'] + ' remove from ' + temp['cca2'])
        print(defaults['cca2'] + ' successfully removed.')
      else:
        print('Nothing to delete. File ' + defaults['cca2'] + '.visa.json does not exist.')