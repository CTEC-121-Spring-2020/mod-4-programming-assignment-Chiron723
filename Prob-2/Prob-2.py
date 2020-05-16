# Module 5
#   Programming Assignment 6
#       Prob-2.py

# <Stephen Guild>

from graphics import *

def main():
     #open Graphics window
     win = GraphWin()

     #Draw a square
     #Changed the shape from a circle to a square, and gave the points mirrored coordinates.
     shape = Rectangle(Point(30,70), Point(70,30))
     shape.setOutline("red")
     shape.setFill("red")
     shape.draw(win)

     #An accumulator pattern to draw copies of the square.
     for i in range(5):
          p = win.getMouse()
     #changed getCenter() to getP1()
          c = shape.getP1()
          dx = p.getX() - c.getX()
          dy = p.getY() - c.getY()
     #removed shape.move(dx,dy) and replaced it with clone system.
          copySquare=shape.clone()
          copySquare.draw(win)
          copySquare.move(dx,dy)
     
     #code to add text at the end before clicking the window to close it.
     #added text after accumulator code.
     endText=Text(Point(100,100),"Click again to quit")
     endText.draw(win)
     #changed close condition to getMouse.
     win.getMouse()

main()