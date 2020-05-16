# Module 5
#   Programming Assignment 6
#       Prob-4.py

# <Stephen Guild>
from graphics import *
def main():
    win=GraphWin("House",600,600)
    #p1 and p2 gives the points neccessary to create the frame using mouse clicks.
    p1=win.getMouse()
    p2=win.getMouse()
    #draws the frame.
    frame=Rectangle(p1,p2)
    frame.draw(win)
    #sets coordinates for both x,y coordinates in main rectangle.
    frameBottomY=max(p1.getY(),p2.getY())
    frameTopY=min(p1.getY(),p2.getY())
    frameLeftX=min(p1.getX(),p2.getX())
    frameRightX=max(p1.getX(),p2.getX())
    #sets the variables for the door.
    p3=win.getMouse()
    doorWidth=abs(p1.getX()-p2.getX())/5
    doorHeight=abs(p3.getY()-frameBottomY)
    doorP1=Point(p3.getX()-doorWidth/2,frameBottomY)
    doorP2=Point(p3.getX()+doorWidth/2,p3.getY())
    #draws the door.
    door=Rectangle(doorP1,doorP2)
    door.draw(win)
    #sets the variables for the window.
    p4=win.getMouse()
    windowHeight=doorWidth/2
    windowP1=Point(p4.getX()-windowHeight/2,p4.getY()-windowHeight/2)
    WindowP2=Point(p4.getX()+windowHeight/2,p4.getY()+windowHeight/2)
    #draws the window.
    window=Rectangle(windowP1,WindowP2)
    window.draw(win)
    #sets the variables for the window.
    p5=win.getMouse()
    roofP1=Point(frameLeftX,frameTopY)
    roofP2=Point(frameRightX,frameTopY)
    roofP3=p5
    #draws the roof.
    roof=Polygon(roofP1,roofP2,roofP3)
    roof.draw(win)

    win.getMouse()


main()