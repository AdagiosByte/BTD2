import pyautogui
import random
import time
from csv import writer

#csv files created
def addTowerToCsv(elementList):
    with open('game.csv','a+',newline='') as csv:
        csv_writer = writer(csv)
        csv_writer.writerow(elementList)

#check tower placement
def checkTower():
    a = pyautogui.screenshot()
    i = a.getpixel((770,606))
    #checks for sell option
    if i[0] == 177 and i[1] == 70 and i[2] == 85:
        return True
    return False

#difficulties and tower placement
def easy(items):
    if i[2] > 250 and i[0] < 200:
        pyautogui.click()
        if checkTower() == True:
            addTowerToCsv(items)
        return True
    elif i[0] == 255 and i[1] == 255 and i[2] == 255:
        return True
    
    
def medium(items):
    if i[0] > 100 and i[1] > 100 and i[2] > 100:
        pyautogui.click()
        return True
    return False
def hard(items):
    if i[0] > 100 and i[1] > 100 and i[2] > 100:
        pyautogui.click()
        return True
    return False

#tower select
def dart():
    pyautogui.click(780,200) # buy dart monkey
    global towerType
    towerType = 0
def cannon():
    pyautogui.click(980,200) # buy cannon
    global towerType
    towerType = 1
def boomerang():
    pyautogui.click(900,250) # buy boomerang
    global towerType
    towerType = 2
    
    
#pop balloons that almost made it to the end
def roadSpikes(difficulty):
    a = pyautogui.screenshot()
    
    if difficulty == 0:
        i = a.getpixel((550,660))
        if i[0] != 255 or i[1] != 255 or i[2] != 255:
            pyautogui.click(780,250) # buy road spikes
            pyautogui.moveTo(550,660)
            pyautogui.click()
    elif difficulty == 1: #WIP
        i = a.getpixel((550,660))
        if i[0] != 255 or i[1] != 255 or i[2] != 255:
            pyautogui.click(780,250) # buy road spikes
            pyautogui.click(550,660)
    else: #WIP
        i = a.getpixel((550,660))
        if i[0] != 255 or i[1] != 255 or i[2] != 255:
            pyautogui.click(780,250) # buy road spikes
            pyautogui.click(550,660)

gameOver = False
placedTower = True
towerType = -1

tower = {0:dart, 1:cannon, 2:boomerang}
stage = {0:easy, 1:medium, 2:hard}

#determine difficulty selected
a = pyautogui.screenshot()
i = a.getpixel((100,100))

if i[2] >200:
    difficulty = 0
elif i[2] > 55:
    difficulty = 1
else:
    difficulty = 2

while gameOver == False:
    lx,ly = 200,200
    tower[random.randint(0,2)]() # select tower
    while placedTower == False:
        
        
        #check for game over (win or loose)
        pyautogui.moveTo(440,170)
        a = pyautogui.screenshot()
        i = a.getpixel((440,170))
        #variable only works on Easy
        j = a.getpixel((440,400))
        
        if i[0] == 30 or j[0] == 255 and j[1] == 62 and j[1] == 62: 
            gameOver = True
            break
        
        pyautogui.moveTo(random.randint(40,720),random.randint(40,700)) #select random tower placement
        
        x,y = pyautogui.position()
        i = a.getpixel((x-60,y))
        
        items = [x,y,difficulty,towerType]
        
        
        #place tower
        placedTower = stage[difficulty](items)
        if placedTower == True:
            lx = x
            ly = y
        
        towerType = -1
        
        
    pyautogui.click(lx,ly) # click last purchaced tower
    pyautogui.moveTo(800,500) # buy left upgrade
    time.sleep(.1)
    pyautogui.click()
    pyautogui.click(900,500) # buy right upgrade
    roadSpikes(difficulty)
    pyautogui.moveTo(900,700) # press Start Round
    pyautogui.click()
    placedTower = False
    
    
    