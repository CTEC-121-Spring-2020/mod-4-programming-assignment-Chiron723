# Module 5
#   Programming Assignment 6
#       Prob-5.py

# <Stephen Guild>
from graphics import *
def main():
    win=GraphWin("Car", 800, 700)
    antenna=Line(Point(500,400),Point(500,500))
    antenna.setOutline("black")
    antenna.draw(win)
    carBody=Rectangle(Point(50,600),Point(650,500))
    carBody.setFill("red")
    carBody.draw(win)
    rearBumper=Rectangle(Point(45,600),Point(100,550))
    rearBumper.setFill("grey")
    rearBumper.draw(win)
    frontBumper=rearBumper.clone()
    frontBumper.move(570,0)
    frontBumper.draw(win)
    carRoof=Polygon(Point(150,500),Point(500,500),Point(450,425),Point(200,425))
    carRoof.setFill("red")
    carRoof.draw(win)
    window=Polygon(Point(160,500),Point(490,500),Point(440,435),Point(210,435))
    window.setFill("cyan")
    window.draw(win)
    backWheel=Circle(Point(200,600),50)
    backWheel.setFill("black")
    backWheel.draw(win)
    backHubcap=Circle(Point(200,600),30)
    backHubcap.setFill("grey")
    backHubcap.draw(win)
    frontWheel=backWheel.clone()
    frontWheel.move(300,0)
    frontWheel.draw(win)
    frontHubcap=backHubcap.clone()
    frontHubcap.move(300,0)
    frontHubcap.draw(win)

    win.getMouse()


main()