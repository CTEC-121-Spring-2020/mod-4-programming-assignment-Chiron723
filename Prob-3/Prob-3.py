# Module 5
#   Programming Assignment 6
#       Prob-3.py

# <Stephen Guild>
from graphics import *
def main():
    win=GraphWin()
    whiteRing = Circle(Point(100,100), 100)
    whiteRing.setOutline("black")
    whiteRing.setFill("white")
    whiteRing.draw(win)
    blackRing = Circle(Point(100,100), 80)
    blackRing.setOutline("black")
    blackRing.setFill("black")
    blackRing.draw(win)
    blueRing = Circle(Point(100,100), 60)
    blueRing.setOutline("black")
    blueRing.setFill("blue")
    blueRing.draw(win)
    redRing = Circle(Point(100,100), 40)
    redRing.setOutline("black")
    redRing.setFill("red")
    redRing.draw(win)
    xRing = Circle(Point(100,100), 20)
    xRing.setOutline("black")
    xRing.setFill("yellow")
    xRing.draw(win)
    win.getMouse()

main()    