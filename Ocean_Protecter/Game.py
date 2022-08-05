'''
Eric,
Jan 29th.
ICS3U1-03,
Mrs.Bokhari
The program runs a game called "The Ocean protector".
Referred to some code in the "collision" video lesson. 
'''

#import library
from pygame import *
import random
from PIL import Image

#initialize
init()

#load fonts
font1 = font.Font('DancingScript-Regular.otf', 50)
font2 = font.Font('LifeSavers-Regular.ttf', 30)
font3 = font.Font('LifeSavers-Regular.ttf', 20)

#Assign RGB values
RED = (255, 0, 0)
BLACK = (0,0,0)
YELLOW = (164, 168, 50)
WHITE=(255,255,255)
GREEN = (50, 168, 82)

#Set width and height
width = 1000
height = 700

#Set up screen
SIZE = (width, height)
screen = display.set_mode(SIZE)

#Load background images 
background = image.load('background.jpg')
background1 = image.load('background1.png')
background2 = image.load('background2.png')
background3 = image.load('background3.png')
background4 = image.load('background4.png')
background5 = image.load('background5.png')
startBackground = image.load('backgroundStart.jpg')

#Load game object images 
case = image.load('case.png')
cpu = image.load('cpu.png')
gpu = image.load('gpu.png')
keyboard = image.load('keyboard.png')
battery = image.load('battery.png')
recycling = image.load('Recyclin.png')
hazer = image.load('bin.png')

#Load buttons images
startButton = image.load('clickedStartIcon.png')
quitButton = image.load('clickedQuitIcon.png')
rulesButton = image.load('Rules.png')
title = image.load('Title.png')

#Load sounds
soundEff = mixer.Sound('bonus.mp3')
soundEff1 = mixer.Sound('bonus1.mp3')
soundEff.set_volume(0.1)
soundEff1.set_volume(0.05)
backgroundMusic = mixer.Sound("backgroundmusic.mp3")
backgroundMusic.set_volume(0.02)

#Change image scale
background = transform.scale(background,(1000,700))
startBackground = transform.scale(startBackground,(1000,700))
keyboard = transform.scale(keyboard,(100,100))
case = transform.scale(case,(100,100))
cpu = transform.scale(cpu,(100,100))
gpu = transform.scale(gpu,(100,100))
battery = transform.scale(battery,(100,100))
recycling = transform.scale(recycling,(100,100))
hazer = transform.scale(hazer,(100,100))

#Add clock
myClock = time.Clock()

#Background List
backgroundList = [background,background1,background2,background3,background4,background5]

#Draw game scene
def drawScreen(foodX,foodY,batX,batY,batX1,batY1,playerX,playerY,point,temp,Recycle,backgroundNum):
    #Each background in backgroundList is different, changes based on another function.
    screen.blit(backgroundList[backgroundNum],(0,0))
    if temp == 0:
        drawFood(foodX,foodY)  
    elif temp == 1:
        drawFood1(foodX,foodY)
    elif temp == 2:
        drawFood2(foodX,foodY)
    elif temp == 3:
        drawFood3(foodX,foodY) 
  
    drawBat1(batX,batY)
    drawBat2(batX1,batY1)
    drawPlayer(playerX,playerY,Recycle)
    showPoint(point)
    showTip()
    display.flip()

#Show point on top left
def showPoint(point):
    score = font1.render("Score :"+ str(point) , True, WHITE)
    screen.blit(score,(10,10))
    
#Show tip to exit out of each screen
def showTip():
    tips = font3.render("Press q to go back",True,WHITE)
    screen.blit(tips,(830,30))
    
#Draw different kinds of objects in game
def drawFood(x,y):
    screen.blit(keyboard,(x,y))
def drawFood1(x,y):
    screen.blit(case,(x,y))
def drawFood2(x,y):
    screen.blit(cpu,(x,y))
def drawFood3(x,y):
    screen.blit(gpu,(x,y))
def drawBat1(x,y):
    screen.blit(battery,(x,y))
def drawBat2(x,y):
    screen.blit(battery,(x,y))

#Draw player
def drawPlayer(x,y,Recycle): 
    if Recycle == True:
        screen.blit(recycling,(x,y))
    elif Recycle == False:
        screen.blit(hazer,(x,y))
        
#Check if x and y collides 
def checkForCollision(x,y):
    if x.colliderect(y):
        return True
    return False

#Point system
def checkPoint(point,temp,Recycle):
    if temp == 0 and Recycle == True:
        point += 3
        soundEff.play()
    if temp == 0 and Recycle == False:
        point -= 1
    if temp == 1 and Recycle == True:
        point += 4
        soundEff.play()
    if temp == 1 and Recycle == False:
        point -= 2
    if temp == 2 and Recycle == True:
        point += 5
        soundEff.play()
    if temp == 2 and Recycle == False:
        point -= 3
    if temp == 3 and Recycle == True:
        point += 7
        soundEff.play()
    if temp == 3 and Recycle == False:
        point -= 4
        
    return point

#Main menu
def selectScreen():
    select = True
    backgroundMusic.play(-1)
    #Button x,y values
    button1X = 150
    button1Y = 450
    
    button2X = 630
    button2Y = 445
    
    button3X = 400
    button3Y = 445
    
    button = 0
    button1 = Image.open("clickedStartIcon.png")

    width1,height1 = button1.size
    width2 = width1-40

    quitbutton = transform.scale(quitButton,(width2,height1))
    rulesbutton = transform.scale(rulesButton,(width2,height1))
    
    button1Rect = Rect(button1X,button1Y,width1,height1)
    button2Rect = Rect(button2X,button2Y,width2,height1)
    rulesRect = Rect(button3X,button3Y,width2,height1)
    
    #Draw the buttons
    screen.fill(WHITE)
    screen.blit(startBackground,(0,0))
    screen.blit(startButton,(button1X,button1Y))
    screen.blit(quitbutton,(button2X,button2Y))
    screen.blit(rulesbutton,(button3X,button3Y))
    screen.blit(title,(75,200))
    
    #Main loop of the main menu
    while select:
        #Get mouse position
        mx, my = mouse.get_pos()
        #Treat mouse as a Rect
        mouseRect = Rect(mx,my,1,1)
        #60 fps
        myClock.tick(60)
        for evnt in event.get():
            if evnt.type == QUIT:
                select = False
                quit()
            if evnt.type == MOUSEBUTTONDOWN:
                button = evnt.button
            else:
                button = 0
            # Check which button is being clicked
            if checkForCollision(mouseRect,button1Rect):
                if button == 1:
                    select = False
                    game_loop()
            if checkForCollision(mouseRect,button2Rect):
                if button == 1:
                    select = False
                    #quit()
            if checkForCollision(mouseRect,rulesRect) and button == 1:
                select = False
                rules()
        display.flip()
        if select == False:
            quit()
            
#Rules scene
def rules():
    run = True
    button = 0
    
    #Reset background
    screen.fill(WHITE)
    screen.blit(startBackground,(0,0))
    
    #Write the messages
    text1 = font2.render("You are the ocean protector.", True, BLACK)
    
    text2 = font2.render("Your job is to recycle different types", True, BLACK)
    text3 = font2.render("of computer hardware correctly.", True, BLACK)
    
    text4 = font2.render("Batteries are considered the most dargerous waste of all, the Ocean can only", True, BLACK)
    text5 = font2.render("survive from no more than five batteries' pollution.", True, BLACK)
    
    text6 = font2.render("Only the hazardous waste bin can obtain batteries. Press 1 to have your ", True, BLACK)
    text7 = font2.render("recycling bin, 2 for the hazardous waste bin.", True, BLACK)
    
    text8 = font2.render("Use arrow keys to control your bin, try to protect", True, BLACK)
    text9 = font2.render("the ocean from pollution!", True, BLACK)

    text10 = font3.render("Right click to go back.",True,BLACK)
    
    #Print it on the screen
    screen.blit(text1,(10,30))
    
    screen.blit(text2,(10,110))
    screen.blit(text3,(10,170))
    
    screen.blit(text4,(10,250))
    screen.blit(text5,(10,310))
    
    screen.blit(text6,(10,390))
    screen.blit(text7,(10,450))
    
    screen.blit(text8,(10,530))
    screen.blit(text9,(10,590))
    
    screen.blit(text10,(800,650))
    display.flip()
    
    while run: 
        for evnt in event.get():
            if evnt.type == QUIT:
                quit()
            if evnt.type == MOUSEBUTTONDOWN:  
                button = evnt.button
            # If right click happns, return to the main menu
            if button == 3:
                run = False
                selectScreen()
                
#Game over screen
def show_go_screen(point):
    #Reset background
    screen.blit(background,(0,0))
    #Load messages
    GG = font1.render("Game Over!", True, WHITE)
    
    Final_score = font1.render( "Your final score is "+str(point), True, WHITE)
    
    Replay = font1.render( "Press a key to play again", True, WHITE)
    
    #Print messages 
    screen.blit(GG,(300, 200))
    screen.blit(Final_score,(300, 350))
    screen.blit(Replay,(300, 500))
    
    myClock.tick(60)
    display.flip()
    
    waiting = True
    while waiting:
        for evnt in event.get():
            if evnt.type == QUIT:
                quit()
            #If any key that is not 'q' is being pressed, reboot the game after 3 seconds
            if evnt.type == KEYUP:
                if evnt.key == K_q:
                    waiting = False
                    selectScreen()
                else:
                    waiting = False
                    time.delay(3000)
                    game_loop()

#Main game loop
def game_loop():
    #Player x,y coordinate and speed
    playerX = 0
    playerY = 550
    playerS = 12
    
    #Object 1 x,y coordinate 
    foodX = random.randint(0, width-100)
    foodY = 0
    
    #Object 2 x,y coordinate 
    batteryX = random.randint(0, width-100)
    batteryY = 0
    
    #Object 3 x,y coordinate     
    batteryX1 = random.randint(0, width-100)
    batteryY1 = 0
    
    #temp value for if functions
    n = 1
    temp = random.randint(0,3)
    
    #Make sure you can continue pressing on a key
    KEY_RIGHT = False
    KEY_LEFT = False
    
    #State of player 
    Recycle = True
    
    #Same as run
    gameexit = False
    
    #Point
    point = 0  
    
    #Object speed
    foodSpeed = [3,4,6,7]
    batSpeed = [4,5]
    
    #The index of background in a list that it will display
    backgroundNum = 0
    

    
    #Main loop
    while not gameexit:
        
        #Uses drawScreen function to draw everything on screen 
        drawScreen(foodX,foodY,batteryX,batteryY,batteryX1,batteryY1,playerX,playerY,point,temp,Recycle,backgroundNum)
        

        #Key press events
        for evnt in event.get():
            if evnt.type == QUIT:
                quit()
            if evnt.type == KEYDOWN:
                if evnt.key == K_LEFT:
                    KEY_LEFT = True
                if evnt.key == K_RIGHT:
                    KEY_RIGHT = True
                if evnt.key == K_1:
                    Recycle = True
                if evnt.key == K_2:
                    Recycle = False
                    
            if evnt.type == KEYUP:
                if evnt.key == K_LEFT:
                    KEY_LEFT = False
                if evnt.key == K_RIGHT:
                    KEY_RIGHT = False
                if evnt.key == K_q:
                    gameexit=False
                    selectScreen()
                    
                    
                    
        #Control player movemnt
        if KEY_LEFT == True and playerX >= 0:
            playerX -= playerS  
        if KEY_RIGHT == True and playerX +100 <= width:
            playerX += playerS
        
        #Set each object into a specific Rect for collision checking
        playerRect = Rect(playerX,playerY, 100, 100)
        foodRect = Rect(foodX ,foodY, 100, 100)
        batRect = Rect(batteryX,batteryY,100,100)
        batRect1 = Rect(batteryX1,batteryY1,100,100)
        
        #Movement of each object 
        foodY += foodSpeed[temp]
        batteryY += batSpeed[0]
        batteryY1 += batSpeed[1]
        
        #Checks for collision when a hardware(foodRect) collides with playerRect
        if checkForCollision(playerRect,foodRect) == True:
            #Check how much the hardware is worth in points, whether or not it was being recycled 
            point = checkPoint(point,temp,Recycle)
            
            #Reset x,y coordinates and produce a new object
            foodY = 0
            foodX = random.randint(0, width-100)
            temp = random.randint(0,3)

        #When battery #1 collides with player, puts battery into recycling bin
        if checkForCollision(playerRect,batRect) == True and Recycle == True:
            #background/ocean gets darker
            backgroundNum += 1
            #Reset object
            batteryX = random.randint(0, width-100)
            batteryY = 0
        #When battery #1 collides with player, battery into hazardous bin.
        elif checkForCollision(playerRect,batRect) == True and Recycle == False:
            point += 5
            soundEff.play()
            batteryX = random.randint(0, width-100)
            batteryY = 0

        #When battery #2 collides with player, puts battery into recycling bin 
        if checkForCollision(playerRect,batRect1) == True and Recycle == True:
            #background/ocean gets darker
            backgroundNum += 1
            batteryX1 = random.randint(0, width-100)
            batteryY1 = 0
        #When battery #2 collides with player, battery into hazardous bin.   
        elif checkForCollision(playerRect,batRect1) == True and Recycle == False:
            point += 5
            soundEff.play()
            batteryX1 = random.randint(0, width-100)
            batteryY1 = 0

        #If hardware(food) goes out of bound
        if foodY >= height:
            point -= 5
            #Reset
            temp = random.randint(0,3)
            foodX = random.randint(0, width-100)
            foodY = 0
        #If battery #1 goes out of bound
        if batteryY >= height:
            backgroundNum += 1
            batteryX = random.randint(0, width-100)
            batteryY = 0
            
        #If battery #2 goes out of bound
        if batteryY1 >= height:
            backgroundNum += 1
            batteryX1 = random.randint(0, width-100)
            batteryY1 = 0
            
        #If point reaches over a multiple of 100, play a sound effect
        if point >= n * 100:
            soundEff1.play()
            n += 1
        #If the ocean gets very dark, game over screen. 
        if backgroundNum == 5:
            gameexit = True
            show_go_screen(point)
        
        myClock.tick(60)
    display.flip()
    
#Run the main menu
selectScreen()
quit()
