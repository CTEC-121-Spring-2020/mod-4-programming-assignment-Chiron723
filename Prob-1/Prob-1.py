# Module 5
#   Programming Assignment 6
#       Prob-1.py

# <Stephen Guild>

# INSTRUCTIONS:
#   Insert a comment above each line of code in the program below to describe
#   what the code does


from graphics import *

def main():
     #opens the graphics window.
     win = GraphWin()
     #Creates a circle that has a center point of 50 for x and y coordinates and a radius of 20.
     shape = Circle(Point(50,50), 20)
     #sets the outline color to red.
     shape.setOutline("red")
     #colors the inside red.
     shape.setFill("red")
     #finalizes the circle and outputs it to the graphics window.
     shape.draw(win)
     #creates an accumulator pattern to be used 5 times.
     for i in range(5):
     # pauses the window waiting for a mouse click in the window.
          p = win.getMouse()
     #Returns a clone of the center point of the circle.
          c = shape.getCenter()
     #creates the difference between the original x and the newly created x.
          dx = p.getX() - c.getX()
     #creates the difference between the original y and the newly created y.
          dy = p.getY() - c.getY()
     #Moves the existing coordinates for the circle to a new position.
          shape.move(dx,dy)
     #closes the window
     win.close()

main()