# Module 5
#   Programming Assignment 6
#       Prob-6.py

# <Stephen Guild>
from graphics import *
def main():
    win = GraphWin("Legos",1100,1000)
    # draw basic brick
    blueBrick = Rectangle(Point(10,280), Point(510, 100))
    blueBrick.setFill("blue")
    blueBrick.setOutline("black")
    blueBrick.setWidth(5)
    blueBrick.draw(win)
    # draw first nib
    blueBrickNib = Rectangle(Point(35, 100), Point(85, 80))
    blueBrickNib.setFill("blue")
    blueBrickNib.setOutline("black")
    blueBrickNib.setWidth(5)
    blueBrickNib.draw(win)
    # test
    for i in range(1, 5):
        blueBrickNextNib = blueBrickNib.clone()
        blueBrickNextNib.move(100 *i, 0)
        blueBrickNextNib.draw(win)
    
    #draw green basic brick
    greenBrick=blueBrick.clone()
    greenBrick.setFill("green")
    greenBrick.move(550,0)
    greenBrick.draw(win)
    #draw first nib
    greenBrickNib=blueBrickNib.clone()
    greenBrickNib.setFill("green")
    greenBrickNib.move(550,0)
    greenBrickNib.draw(win)
    #test
    for i in range(1,5):
        greenBrickNextNib = greenBrickNib.clone()
        greenBrickNextNib.move(100 *i, 0)
        greenBrickNextNib.draw(win)

    #draw yellow basic brick
    yellowBrick=blueBrick.clone()
    yellowBrick.setFill("yellow")
    yellowBrick.move(0,250)
    yellowBrick.draw(win)
    #draw first nib
    yellowBrickNib=blueBrickNib.clone()
    yellowBrickNib.setFill("yellow")
    yellowBrickNib.move(0,250)
    yellowBrickNib.draw(win)
    #test
    for i in range(1,5):
        yellowBrickNextNib = yellowBrickNib.clone()
        yellowBrickNextNib.move(100 *i, 0)
        yellowBrickNextNib.draw(win)

    #draw red basic brick
    redBrick=greenBrick.clone()
    redBrick.setFill("red")
    redBrick.move(0,250)
    redBrick.draw(win)
    #draw first nib
    redBrickNib=greenBrickNib.clone()
    redBrickNib.setFill("red")
    redBrickNib.move(0,250)
    redBrickNib.draw(win)
    #test
    for i in range(1,5):
        redBrickNextNib = redBrickNib.clone()
        redBrickNextNib.move(100 *i, 0)
        redBrickNextNib.draw(win)
    
    #draw cyan basic brick
    cyanBrick=yellowBrick.clone()
    cyanBrick.setFill("cyan")
    cyanBrick.move(0,250)
    cyanBrick.draw(win)
    #draw first nib
    cyanBrickNib=yellowBrickNib.clone()
    cyanBrickNib.setFill("cyan")
    cyanBrickNib.move(0,250)
    cyanBrickNib.draw(win)
    #test
    for i in range(1,5):
        cyanBrickNextNib = cyanBrickNib.clone()
        cyanBrickNextNib.move(100 *i, 0)
        cyanBrickNextNib.draw(win)

    #draw black basic brick
    blackBrick=cyanBrick.clone()
    blackBrick.setFill("black")
    blackBrick.setOutline("red")
    blackBrick.move(550,0)
    blackBrick.draw(win)
    #draw first nib
    blackBrickNib=cyanBrickNib.clone()
    blackBrickNib.setFill("black")
    blackBrick.setOutline("red")
    blackBrickNib.move(550,0)
    blackBrickNib.draw(win)
    #test
    for i in range(1,5):
        blackBrickNextNib = blackBrickNib.clone()
        blackBrickNextNib.move(100 *i, 0)
        blackBrickNextNib.draw(win)

    win.getMouse()

main()