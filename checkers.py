import inspect
def checkersPage():
   global joining 
   global move 
   
   SQUAREWIDTH = 50
   BOARDY = 50
   BOARDX = 100 
   RADIUS = int((SQUAREWIDTH/2) - 10)
   OFFSET = 0   
      
   def inBoard (x,y):
      insideBoard = False
      if (x >= BOARDX) and (y >= BOARDY):
         if (x <= (BOARDX+(8*SQUAREWIDTH))) and (y <= (BOARDY+(8*SQUAREWIDTH))): 
            insideBoard = True
      return insideBoard
      
   def legalMove (x1,y1,x2,y2):
      return True
      
   def drawBoard(): 
      DISPLAYSURF.fill((WHITE)) 
      y = BOARDY
      count = 0
      for i in range (8):
         for j in range (8):
            count = count + 1
            x = BOARDX + (j * SQUAREWIDTH)
            if (count % 2) == 1:
               pygame.draw.rect(DISPLAYSURF, BLACK, (x,y,SQUAREWIDTH, SQUAREWIDTH))
            else:                  
               pygame.draw.rect(DISPLAYSURF, RED, (x,y,SQUAREWIDTH, SQUAREWIDTH))
         y = y + SQUAREWIDTH
         count = count + 1 # stagger the colors   
   
      y = BOARDY
      count = 0
      for piece in redPieces:
         x = piece[0]
         y = piece[1]
         print ( 'Place redPiece at [' + str(x) + ',' + str(y) + ']') 
         DISPLAYSURF.blit (redImages[count], (x,y))         
         count = count + 1
         
      count = 0
      for piece in blackPieces:
         x = piece[0]
         y = piece[1]
         print ( 'Place blackPiece at [' + str(x) + ',' + str(y) + ']') 
         DISPLAYSURF.blit (blackImages[count], (x,y))
         count = count + 1

      pygame.display.update()        
            
   # Show screen
   pygame.display.set_caption('Play Checkers')        

   (redImages,redPieces) = showImages (['redChecker.png', 'redChecker.png', 'redChecker.png', 'redChecker.png', 'redChecker.png', 'redChecker.png', 'redChecker.png', 'redChecker.png', 'redChecker.png', 'redChecker.png', 'redChecker.png', 'redChecker.png', 'redChecker.png', 'redChecker.png', 'redChecker.png', 'redChecker.png'], \
                           [(BOARDX+OFFSET,BOARDY+OFFSET) , \
                            (BOARDX+OFFSET+(SQUAREWIDTH*1),BOARDY+OFFSET), \
                            (BOARDX+OFFSET+(SQUAREWIDTH*2),BOARDY+OFFSET), \
                            (BOARDX+OFFSET+(SQUAREWIDTH*3),BOARDY+OFFSET), \
                            (BOARDX+OFFSET+(SQUAREWIDTH*4),BOARDY+OFFSET), \
                            (BOARDX+OFFSET+(SQUAREWIDTH*5),BOARDY+OFFSET), \
                            (BOARDX+OFFSET+(SQUAREWIDTH*6),BOARDY+OFFSET), \
                            (BOARDX+OFFSET+(SQUAREWIDTH*7),BOARDY+OFFSET), \
                            (BOARDX+OFFSET,                BOARDY+OFFSET+SQUAREWIDTH), \
                            (BOARDX+OFFSET+(SQUAREWIDTH*1),BOARDY+OFFSET+SQUAREWIDTH), \
                            (BOARDX+OFFSET+(SQUAREWIDTH*2),BOARDY+OFFSET+SQUAREWIDTH), \
                            (BOARDX+OFFSET+(SQUAREWIDTH*3),BOARDY+OFFSET+SQUAREWIDTH), \
                            (BOARDX+OFFSET+(SQUAREWIDTH*4),BOARDY+OFFSET+SQUAREWIDTH), \
                            (BOARDX+OFFSET+(SQUAREWIDTH*5),BOARDY+OFFSET+SQUAREWIDTH), \
                            (BOARDX+OFFSET+(SQUAREWIDTH*6),BOARDY+OFFSET+SQUAREWIDTH), \
                            (BOARDX+OFFSET+(SQUAREWIDTH*7),BOARDY+OFFSET+SQUAREWIDTH)  \
                           ] ) 
   redLocations = [ \
                    [0,0], [1,0], [2,0], [3,0], [4,0], [5,0], [6,0], [7,0], \
                    [0,1], [1,1], [2,1], [3,1], [4,1], [5,1], [6,1], [7,1], \
                  ]

   (blackImages,blackPieces) = showImages (['blackChecker.png', 'blackChecker.png', 'blackChecker.png', 'blackChecker.png', 'blackChecker.png', 'blackChecker.png', 'blackChecker.png', 'blackChecker.png', 'blackChecker.png', 'blackChecker.png', 'blackChecker.png', 'blackChecker.png', 'blackChecker.png', 'blackChecker.png', 'blackChecker.png', 'blackChecker.png'], \
                           [(BOARDX+OFFSET,BOARDY+OFFSET+(SQUAREWIDTH*6)) , \
                            (BOARDX+OFFSET+(SQUAREWIDTH*1),BOARDY+OFFSET+(SQUAREWIDTH*6)), \
                            (BOARDX+OFFSET+(SQUAREWIDTH*2),BOARDY+OFFSET+(SQUAREWIDTH*6)), \
                            (BOARDX+OFFSET+(SQUAREWIDTH*3),BOARDY+OFFSET+(SQUAREWIDTH*6)), \
                            (BOARDX+OFFSET+(SQUAREWIDTH*4),BOARDY+OFFSET+(SQUAREWIDTH*6)), \
                            (BOARDX+OFFSET+(SQUAREWIDTH*5),BOARDY+OFFSET+(SQUAREWIDTH*6)), \
                            (BOARDX+OFFSET+(SQUAREWIDTH*6),BOARDY+OFFSET+(SQUAREWIDTH*6)), \
                            (BOARDX+OFFSET+(SQUAREWIDTH*7),BOARDY+OFFSET+(SQUAREWIDTH*6)), \
                            (BOARDX+OFFSET,                BOARDY+OFFSET+(SQUAREWIDTH*7)), \
                            (BOARDX+OFFSET+(SQUAREWIDTH*1),BOARDY+OFFSET+(SQUAREWIDTH*7)), \
                            (BOARDX+OFFSET+(SQUAREWIDTH*2),BOARDY+OFFSET+(SQUAREWIDTH*7)), \
                            (BOARDX+OFFSET+(SQUAREWIDTH*3),BOARDY+OFFSET+(SQUAREWIDTH*7)), \
                            (BOARDX+OFFSET+(SQUAREWIDTH*4),BOARDY+OFFSET+(SQUAREWIDTH*7)), \
                            (BOARDX+OFFSET+(SQUAREWIDTH*5),BOARDY+OFFSET+(SQUAREWIDTH*7)), \
                            (BOARDX+OFFSET+(SQUAREWIDTH*6),BOARDY+OFFSET+(SQUAREWIDTH*7)), \
                            (BOARDX+OFFSET+(SQUAREWIDTH*7),BOARDY+OFFSET+(SQUAREWIDTH*7))  \
                           ] ) 
   blackLocations = [ \
                      [0,6], [1,6], [2,6], [3,6], [4,6], [5,6], [6,6], [7,6], \
                      [0,7], [1,7], [2,7], [3,7], [4,7], [5,7], [6,7], [7,7], \
                    ]
   drawBoard()
   (images,sprites) = showImages (['quit.jpg'], [(400,500)] )      

   showStatus ( "Waiting for player to join")
   pygame.display.update()
   
   if iAmHost:
      # Set opponents list of games
      udpBroadcast ( 'exec:games=[\'Checkers\']')
      joining = ''
      playerJoined = False
      move = (0,0) # Host can move first
      myTurn = True
   else:
      udpBroadcast ( 'exec:joining=\'Checkers\'')
      joining = 'Checkers' # Opponent should be waiting
      move = None
       
   quit = False    
   redSelectedPiece = None
   blackSelectedPiece = None
   while not quit: 
      (eventType,data,addr) = getInput (100,100)
      
      if eventType == pygame.MOUSEBUTTONUP:
         if redSelectedPiece != None: 
            x = int((data[0] - BOARDX) / SQUAREWIDTH)
            y = int((data[1] - BOARDY) / SQUAREWIDTH)
            x = BOARDX + (x * SQUAREWIDTH)
            y = BOARDY + (y * SQUAREWIDTH)
            if legalMove (x,y,x,y): 
               redSelectedPiece[0] = x
               redSelectedPiece[1] = y 
               drawBoard()
               (images,sprites) = showImages (['quit.jpg'], [(400,500)])
               move = None
               udpBroadcast ( 'exec:move=(' + str(x) + ',' + str(y) + ')')               
            else:
               showStatus ('Red illegal move' )
            
         if blackSelectedPiece != None: 
            x = int((data[0] - BOARDX) / SQUAREWIDTH)
            y = int((data[1] - BOARDY) / SQUAREWIDTH)
            x = BOARDX + (x * SQUAREWIDTH)
            y = BOARDY + (y * SQUAREWIDTH)
            if legalMove (x,y,x,y): 
               blackSelectedPiece[0] = x
               blackSelectedPiece[1] = y 
               drawBoard()
               (images,sprites) = showImages (['quit.jpg'], [(400,500)])
               move = None
               # move = (fromX, fromY, toX, toY)
               udpBroadcast ( 'exec:move=(' + str(x) + ',' + str(y) + ',' + str(x) + ',' + str(y)+ ')')               
            else:
               showStatus ( 'Black illegal move' )
         redSelectedPiece = None
         blackSelectedPiece = None  
         
      elif eventType == pygame.MOUSEBUTTONDOWN:
         if myTurn: 
            if joining == 'Checkers':
               if move == None: 
                  showStatus ( 'Waiting for opponent to move')
               else: 
                  piece = getSpriteClick (eventType, data, redPieces)          
                  if piece != -1:
                     redSelectedPiece = redPieces[piece]
                  piece = getSpriteClick (eventType, data, blackPieces)          
                  if piece != -1:
                     print ("black piece clicked on")
                     blackSelectedPiece = blackPieces[piece]
            else:
               showStatus ( 'Waiting for other player to join')
         else:
            showStatus ( 'Waiting for other player to move' )                                  
         
      elif eventType == pygame.MOUSEMOTION:
         if redSelectedPiece != None:
            print ( 'Move redSelectedPiece to: ' + str(data) )
            if inBoard (data[0], data[1]): 
               redSelectedPiece[0] = data[0] - int(SQUAREWIDTH/2)
               redSelectedPiece[1] = data[1] - int(SQUAREWIDTH/2)
            
               drawBoard()
               (images,sprites) = showImages (['quit.jpg'], [(400,500)] )                 
             
         elif blackSelectedPiece != None:
            print ( 'Move blackSelectedPiece to: ' + str(data))  
            if inBoard (data[0], data[1]):
               blackSelectedPiece[0] = data[0] - int(SQUAREWIDTH/2)
               blackSelectedPiece[1] = data[1] - int(SQUAREWIDTH/2)
               drawBoard()
               (images,sprites) = showImages (['quit.jpg'], [(400,500)] )                     

      elif eventType == 'udp':         
         if data.find ( 'move=') > -1: # Opponent has moved 
            fromX = move[0]
            fromY = move[1]
            toX = move[2]
            toY = move[3]
            # Lookup piece given the location
            # Move the piece 
            print ( 'got a udp move' )
         print ( 'Got a udp: [' + data + '] from: ' + addr )
          
      sprite = getSpriteClick (eventType, data, sprites ) 
      if sprite != -1: # Quit is the only other option           
         print ("Selected command: " + str(sprite))
         mainPage (True)
         quit = True    
CHECKERS=inspect.getsource(checkersPage)