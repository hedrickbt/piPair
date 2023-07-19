from images.mtg.ManaCost import ManaCost 
from cardDatabase import cardDatabase 

class Convert():
   def __init__ (self):
      self.manaCost     = ManaCost().cost
      self.cardDatabase = cardDatabase().data
    
   def existingValue (self, directoryList, filename, fieldName, defaultValue): 
      value = defaultValue
      # print ( 'Check: ' + str(directoryList[filename]) ) 
      if fieldName in directoryList[filename]: 
         value = directoryList[filename][fieldName]
      return value         
   
   def oneRow (self,filename,count): 
      row = self.manaCost[filename]   
      '''
      if filename.find ( 'doge') > -1: 
         if filename in self.cardDatabase: 
            print ( 'Doge found in cardDatabase' )
         else:
            print ( 'Doge NOT found in card database ' )
      '''      
      if 'images/mtg/' + filename in self.cardDatabase: 
         if 'power' in self.cardDatabase['images/mtg/' + filename]: 
            row ['power']     = self.cardDatabase['images/mtg/' + filename]['power']
         if 'toughness' in self.cardDatabase['images/mtg/' + filename]: 
            row ['toughness'] = self.cardDatabase['images/mtg/' + filename]['toughness']
         if 'flying' in self.cardDatabase['images/mtg/' + filename]: 
            row ['flying']    = self.cardDatabase['images/mtg/' + filename]['flying']
         if 'haste' in self.cardDatabase['images/mtg/' + filename]: 
            row ['haste']     = self.cardDatabase['images/mtg/' + filename]['haste']
      row ['id']        = count
      return str(row) 
             
   def convertAll (self): 
      msg = '' 
      count = 0
      for filename in self.manaCost: 
         if msg == '': 
            msg = '{ \\\n' 
         else:
            msg = msg + ', \\\n' 
            
         msg = msg + '      \'' + filename + '\':' + self.oneRow (filename,count)
         count = count + 1         
         
      msg = msg + ' \\\n}\n'      
      return msg
      
if __name__ == '__main__':
   convert = Convert()
   f = open ( 'images\mtg\CardInfo.py', 'w')
   f.write ( '# Do not edit this file, it is created by Convert.py\n' )
   f.write ( 'class CardInfo():\n' )
   f.write ( '   cards = ' + convert.convertAll() ) 
   f.write ( '   def idToName (self,id): \n' )
   f.write ( '      name = \'\'\n' )
   f.write ( '      if id <= len(self.cards):\n' )
   f.write ( '         name = list(self.cards)[id]\n' )
   f.write ( '      print ( \'Got name: \' + name )\n' )
   f.write ( '      return (name)\n' )   
   f.write ( '   def isCreature (self,id): \n' )
   f.write ( '      creature = False\n' )
   f.write ( '      name = self.idToName (id)\n' )
   f.write ( '      if name.find ( \'creatures\' ) > -1: \n' )
   f.write ( '         creature = True\n' )
   f.write ( '         print ( \'This is a creature: \' + name )\n' )
   f.write ( '      else:\n' )
   f.write ( '         print ( \'This is NOT a creature: \' + name )\n' )
   f.write ( '      return creature\n' )
   f.close()    
   
   