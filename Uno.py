import inspect
import pygame
import time
from Communications import Communications

from Deck      import Deck
from Utilities import Utilities
from OptionBox import OptionBox
from SubDecks  import SubDecks
from TextBox   import TextBox
from UnoCards  import UnoCards
 
BLACK = (  0,  0,  0)
RED   = (255,  0,  0)
# Show the Uno Pages
class Uno (): 
    def __init__ (self, DISPLAYSURF, utilities, comm ):
       self.comm = comm
       self.DISPLAYSURF = DISPLAYSURF
       self.utilities   = utilities       
       print ( 'Initialization Uno' )
       self.iAmHost     = True   

    def gameOver (self): 
       over = False
       return over
       
    def main (self):
       def handleSubdeck (name,cardsStr):
          print ( 'handleSubdeck [name,cardsStr]: [' + name + ',' + str(cardsStr) + ']' )
          if self.comm.gotPeek ('subdeck uno'):   
             message = self.comm.peek () 
             print ( 'handleSubdeck, got message: [' + message + ']')
             cards = [] 
             for c in cardsStr: 
                cards.append (int(c))             
             if name == 'hand': 
                print ( '*** Adding ' + str(len(cardsStr) ) + ' to hand' ) 
                d = UnoCards (deck, startXY=(100,400), displaySurface=displaySurface, cards=cards)             
             elif name == 'opponent': 
                d = UnoCards (deck, startXY=(100,50),  displaySurface=displaySurface, cards=cards) 
             elif name == 'discardPile': 
                print ( 'Creating a discardPile with xMultiplier = 0.0' );
                d = UnoCards (deck,  startXY=(100,200), displaySurface=displaySurface, xMultiplier=0.0, yMultiplier=0.0, cards=cards)
             elif name == 'drawPile': 
                d = UnoCards (deck,  startXY=(300,200), displaySurface=displaySurface, xMultiplier=0.0, yMultiplier=0.0, cards=cards)
             d.name = name 
             return d
             
       discardPile = None
       print ( 'Uno.main' )
       self.DISPLAYSURF.fill((BLACK))
       displaySurface = self.DISPLAYSURF # refactor out?
       if self.iAmHost: 
          pygame.display.set_caption('Play Uno I am host:' + self.comm.target)        
       else:
          pygame.display.set_caption('Play Uno I am player:' + self.comm.target)        
       
       sprites = self.utilities.showImages (['quit.jpg'], [(400,600)] )
       pygame.display.update()

       deck = Deck ('images/unoSpriteSheet.jpg', 10, 6, 52, 52)
                 
       if self.iAmHost: 
          state = 1   
          self.utilities.showStatus ( "Host, Waiting for player to join")
          hand        = UnoCards (deck,  7, startXY=(100,400), displaySurface=displaySurface)
          opponent    = UnoCards (deck,  7, startXY=(100,50),  displaySurface=displaySurface)
          discardPile = UnoCards (deck,  1, startXY=(100,200), displaySurface=displaySurface, xMultiplier=0.0, yMultiplier=0.0)
          # All remaining cards go into the draw pile 
          drawPile    = UnoCards (deck,  0, startXY=(300,200), displaySurface=displaySurface, xMultiplier=0.0, yMultiplier=0.0)
          print ( 'line 72, drawPile.hideAll' )
          drawPile.hideAll () 
          
          # creates decks array 
          cards=[]
          cards.append (opponent)
          cards.append (drawPile)   
          cards.append (discardPile)
          cards.append (hand)
          decks = SubDecks (cards)    
          
        
          pygame.display.update()
       else: # Host goes first...
          hand = type('SubDeck', (object,), {})()       
          opponent = type('SubDeck', (object,), {})()       
          state = 2
          self.comm.send ( 'join uno' )
          self.utilities.showStatus ( "Waiting for host to deal")
          cards=[]
       
       joinTimeout = 0    
       quit = False 

       # Get/Send Decks        
       if state == 1: 
          self.utilities.showStatus ( "Give Cards")
       else:
          self.utilities.showStatus ( "Get Cards" )
       while True:
          if state == 1: # host 
             if self.comm.gotPeek ( 'join uno' ):
                self.utilities.showStatus ( 'Sending cards to opponent' )
                self.comm.send ( 'subdeck uno opponent '    + hand.cardsToStr () )
                self.comm.send ( 'subdeck uno drawPile '    + drawPile.cardsToStr () )                 
                self.comm.send ( 'subdeck uno discardPile ' + discardPile.cardsToStr() )
                self.comm.send ( 'subdeck uno hand '        + opponent.cardsToStr () )
                self.comm.pop() # Consume peek 
                break
          elif state == 2: # player 
             if self.comm.gotPeek ('subdeck uno'): 
                message = self.comm.peek()
                data = message.split (' ')
                print ( 'data: ' + str(data) ) 
                name     = data[2]                 
                cardsStr = data[3:]
                
                if name == 'opponent': 
                   opponent    = handleSubdeck (name, cardsStr)                 
                elif name == 'hand': 
                   hand        = handleSubdeck (name, cardsStr )
                elif name == 'discardPile': 
                   discardPile = handleSubdeck (name, cardsStr )
                elif name == 'drawPile': 
                   drawPile    = handleSubdeck (name, cardsStr )
                   print ( 'line 127, drawPile.hideAll' )
                   drawPile.hideAll () 
                   
                message = self.comm.pop ()
                   
                # creates decks array 
                if name == 'hand': 
                   cards=[]
                   if opponent is None: 
                      print ( 'line 134, Cannot create decks with a None opponent deck' )
                      exit()
                   cards.append (opponent)
                   cards.append (drawPile)   
                   cards.append (discardPile)
                   cards.append (hand)
                   
                   decks = SubDecks (cards)  
                   print ( 'decks.draw, line 138' )
                   decks.draw()
               
                   break

 
       if discardPile is None: 
          print ( 'ERR discardpile should not be None!' )
          exit()
 
       print ( 'Start while loop state: ')
       myMove = self.iAmHost 
       if myMove: 
          self.utilities.showStatus ( "Your Turn")
       else:
          self.utilities.showStatus ( 'Waiting for opponents move' )
       dragging   = None
       dragDeck   = None
       sourceDeck = None
       offset     = None
       print ( 'line 155, start while loop' )
       while not self.utilities.quit and not self.gameOver() and not quit:
          window = pygame.display.get_surface()    
          window.fill ((0,0,0))  
          TextBox('Opponent', x=100, y=  5).draw()
          TextBox('Discard',  x=100, y=175).draw()
          TextBox('Draw',     x=310, y=175).draw()
          TextBox('Hand',     x=100, y=375).draw()        

          decks.draw() # Show and set their x/y locations 
          sprites = self.utilities.showImages (['quit.jpg'], [(400,600)] )       
          self.utilities.showLastStatus()
          self.utilities.flip() 
          
          if not myMove and self.comm.gotPeek ('uno move'): 
             message = self.comm.pop()
             self.utilities.showStatus ( "Opponent moved, Your Turn")
             myMove = True          
                 
          # pygame.display.update()
          events = self.utilities.readOne()
          for event in events:
             (typeInput,data,addr) = event                                
             # Use data above to determine sprite click?                
             if typeInput == 'drag':  
                sprite = self.utilities.findSpriteClick (event[1], sprites ) 
                if sprite != -1: # Quit is the only other option           
                   print ("Selected command: " + str(sprite))
                   quit = True    
                elif typeInput == 'drag':  ## ? necessary if statement? 
                   if myMove:
                      print ( '\n\n***DRAG***\n\n' )
                      (deck,index) = decks.findSprite (data) # Returns index in list 
                      name = deck.cardName ( deck.data[index].sheetIndex)
                      print ( 'CardName: ' + name )
                      startPos = (deck.data[index].x,deck.data[index].y)                      

                      if deck == opponent: 
                         self.utilities.showStatus ( 'ERR you cannot move an opponents card' )
                      elif deck == discardPile: 
                         self.utilities.showStatus ( 'ERR this is where you drop cards' )
                      elif deck == drawPile:                                         
                         self.utilities.showStatus ( 'Drawing a card with index: ' + str(index) )
                         deck.data[index].hide = False
                         hand.addCard (deck,index)
                         deck.remove (index)                   
                      elif deck == hand:                           
                         sourceDeck = hand
                         mousePos = data
                         self.utilities.showStatus ( 'Hand card: ' + str(index)) 
                         dragging = index                    
                      else:
                         self.utilities.showStatus ( 'Unknown deck' )
                   else: 
                      self.utilities.showStatus ('Err, not your move' )                      
 
             elif typeInput == 'move':
                if not dragging is None: 
                   if offset is None: 
                      pos = deck.pos (dragging)
                      offset = ( pos[0] - data[0], pos[1] - data[1])
                      print ( 'Starting pos: ' + str(pos) + ' mouse: ' + str(data) + ' offset: ' + str(offset))
                   newPos = ( data[0] + offset[0], data[1] + offset[1] );
                   deck.move (dragging,newPos)
                mousePos = data
             elif typeInput == 'drop':
                (deck,index) = decks.findOtherDeck (hand,data) # Where are we dropping
                if deck != discardPile:
                   self.utilities.showStatus ( 'ERR, you can only drop on the discard pile' )                   
                   hand.data[dragging].x = startPos[0]
                   hand.data[dragging].y = startPos[1]
                else:
                   if hand.canDrop (hand.data[dragging].sheetIndex, deck.data[index].sheetIndex): 
                      discardPile.addCard (hand,dragging)                
                      hand.remove (dragging)                   
                      print ( 'discardPile now has ' + str(discardPile.length()) + ' cards' )
                      self.comm.send ( 'uno move' )                                      
                      myMove = False 
                      self.utilities.showStatus ( 'Waiting for opponents move' )
                   else:
                      print ( 'Oops you cannot drop this card here' )
                      # Return card to origin position 
                      hand.data[dragging].x = startPos[0]
                      hand.data[dragging].y = startPos[1]
                    
                dragging = None
                offset = None
             else:
                self.utilities.showStatus ( 'Unknown event: [' + str(event) + ']' )
 
          if self.utilities.quit:
             print ( 'self.utilities.quit' )
          elif self.gameOver(): 
             print ( 'self.gameOver' )
          elif quit: 
             print ( 'quit == True' )          
       print ( 'Go back to the main page...' ) 
    
if __name__ == '__main__':
   try: 
      import sys
      numParameters = len(sys.argv)
      print ( 'number of parameters: ' + str(numParameters) ) 
      
      pygame.init()
      displaySurface = pygame.display.set_mode((1200, 800))
      BIGFONT = pygame.font.Font('freesansbold.ttf', 32)
      
      name = 'pi7'   
      comm = Communications ('messages', 'localhost', name )
      comm.connectBroker()
      comm.setTarget ( 'laptop' )
      print ( 'Back from connectBroker' )
      
      utilities = Utilities (displaySurface, BIGFONT)   
      utilities.comm = comm
      
      uno = Uno(displaySurface,utilities,comm)
      uno.iAmHost = True
      uno.main()       
      
     
   finally: 
      comm.disconnect()