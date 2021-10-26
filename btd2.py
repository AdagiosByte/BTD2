import pyautogui
import random

#difficulties
def easy():
    if i[2] > 250:
            pyautogui.click()
            placedTower = True
def medium():
    if i[0] > 100 and i[1] > 100 and i[2] > 100:
            pyautogui.click()
            placedTower = True
def hard():
    if i[0] > 100 and i[1] > 100 and i[2] > 100:
            pyautogui.click()
            placedTower = True

#towers
def dart():
    pyautogui.click(780,200) # buy dart monkey
def cannon():
    pyautogui.click(980,200) # buy cannon

gameOver = False
placedTower = False

tower = {0:dart, 1:cannon}
stage = {0:easy, 1:medium, 2:hard}

#determine difficulty selected
a = pyautogui.screenshot()
i = a.getpixel((100,100))

if i[2] == 255:
    difficulty = 0
elif i[2] > 55:
    difficulty = 1
else:
    difficulty = 2

while gameOver == False:
    
    tower[random.randint(0,1)]() # select tower
    while placedTower == False:
        
        
        #check for game over (win or loose)
        pyautogui.moveTo(440,300)
        x,y = pyautogui.position()
        i = a.getpixel((x,y))
        if i[1] == 102 or i[1] == 103: 
            gameOver = True
            break
        
        pyautogui.moveTo(random.randint(40,720),random.randint(40,700)) #select random tower placement
        
        x,y = pyautogui.position()
        i = a.getpixel((x-60,y))
        
            
        #place tower
        stage[difficulty]()
        
        
        
    pyautogui.click(800,500) # buy left upgrade
    pyautogui.click(900,500) # buy right upgrade
    pyautogui.click(900,700) # press Start Round
    placedTower = False
    
    
    
    
    
    
    #pyautogui.click(780,250) # buy tack tower