"""

Snake Game made by: @chemokita13

"""

import os # to clear the shell
import random # for random numbers ( snake food)
from time import sleep # for delay
from pynput import keyboard as kb # for keyboard listener

#* Map size (including borders)
mapWidht = 16 # border in numbres 1, 16
mapHeight = 16 # border in numbres 1, 16

class snake: #* Class Snake

    def __init__(self): #* Constructor
        self.x = 7 # x coordinate
        self.y = 7 # y coordinate
        self.body = [] # body of snake
        self.direction = 'pause' # direction of snake
        self.score = 0 # score of snake
        self.live = True # live of snake
    

    def move(self): #* move snake
        self.body.insert(0, [self.x, self.y]) # add new coordinate to body
        self.body.pop() # remove last coordinate from body
        if self.direction == 'right':
            self.x += 1
        elif self.direction == 'left':
            self.x -= 1
        elif self.direction == 'up':
            self.y -= 1
        elif self.direction == 'down':
            self.y += 1
        elif self.direction == 'pause':
            pass
        for tailPosition in self.body:
            if self.x == tailPosition[0] and self.y == tailPosition[1]:
                self.live = False
                break
        if self.x <= 1 or self.x >= mapWidht or self.y <= 1 or self.y >= mapHeight: #* check if snake is out of map
            self.live = False
        #?print(self.direction, self.x, self.y)

    def eat(self): #* eat food
        if Snake.score == 0:
            self.body.append([self.x, self.y])
        else:
            self.body.append([self.body[-1][0]-1, self.body[-1]]) # add new body part
        self.score += 1 # increase score
        

def food(): #* create food
    x = random.randint(2, mapWidht-2)
    y = random.randint(2, mapHeight-2)
    return [x, y]

def drawMap(): #* draw map
    
    global Food, Snake #* global variables

    os.system("cls") # clear shell

    for y in range(1, mapHeight): # vertical lines

        for x in range(1, mapWidht): # horizontal lines
            if x == 1 or x == mapWidht-1 or y == 1 or y == mapHeight-1:
                print('#', end='')
            else:
                #** prints snake
                if Snake.x == x and Snake.y == y: # prints snake head
                    print('O', end='')
                elif [x, y] in Snake.body: # prints snake body
                    print('o', end='')
                elif x == Food[0] and y == Food[1]: # prints food
                    print('*', end='')
                else:
                    print(' ', end='')

        print()
    print('Score:', Snake.score)
    if Snake.x == Food[0] and Snake.y == Food[1]:
        Snake.eat()
        Food = food()

def keyPress(key): #* key press
    Key = str(key)
    if (Key == 'Key.up' or Key == "'w'") and Snake.direction != 'down':
        Snake.direction = 'up'
    elif Key == 'Key.down' or Key == "'s'" and Snake.direction != 'up':
        Snake.direction = 'down'    
    elif Key == 'Key.left' or Key == "'a'" and Snake.direction != 'right':
        Snake.direction = 'left'
    elif Key == 'Key.right' or Key == "'d'" and Snake.direction != 'left':
        Snake.direction = 'right'
    elif Key == 'Key.esc':
        return False
    

#** Main
Snake = snake() #* create snake (obj)

keyboardListener = kb.Listener(keyPress) # create keyboard listener
keyboardListener.start() #* start keyboard listener

Food = food() #* create food

while Snake.live: #* while snake is live
    Snake.move() # moving snake
    drawMap() # drawing map
    sleep(0.1) #* delay
else:
    os.system('cls')
    print(' Score:', Snake.score)
    print(" Game Over :(") #* Game Over