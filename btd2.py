import pyautogui
import random
import time

#difficulties
def easy():
    if i[2] > 250 and i[0] < 200:
        pyautogui.click()
        return True
    elif i[0] == 255 and i[1] == 255 and i[2] == 255:
        return True
    
    
def medium():
    if i[0] > 100 and i[1] > 100 and i[2] > 100:
        pyautogui.click()
        return True
    return False
def hard():
    if i[0] > 100 and i[1] > 100 and i[2] > 100:
        pyautogui.click()
        return True
    return False

#towers
def dart():
    pyautogui.click(780,200) # buy dart monkey
def cannon():
    pyautogui.click(980,200) # buy cannon
def boomerang():
    pyautogui.click(900,250) # buy boomerang

gameOver = False
placedTower = True


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
    
    tower[random.randint(0,2)]() # select tower
    while placedTower == False:
        
        
        #check for game over (win or loose)
        pyautogui.moveTo(440,170)
        a = pyautogui.screenshot()
        i = a.getpixel((440,170))
        if i[0] == 30: 
            gameOver = True
            break
        
        pyautogui.moveTo(random.randint(40,720),random.randint(40,700)) #select random tower placement
        
        x,y = pyautogui.position()
        i = a.getpixel((x-60,y))
        
            
        #place tower
        placedTower = stage[difficulty]()
        
        
    pyautogui.moveTo(800,500) # buy left upgrade
    time.sleep(.1)
    pyautogui.click()
    pyautogui.click(900,500) # buy right upgrade
    pyautogui.moveTo(900,700) # press Start Round
    pyautogui.click()
    placedTower = False
    
    
    #pyautogui.click(780,250) # buy tack tower