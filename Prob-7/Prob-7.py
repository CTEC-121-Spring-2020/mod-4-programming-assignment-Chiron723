# Module 5
#   Programming Assignment 6
#       Prob-7.py

# <Stephen Guild>
from graphics import *
def main():
    win=GraphWin("face",500,500)
    #Ears
    leftEar=Circle(Point(100,250),30)
    leftEar.setFill("cyan")
    leftEar.draw(win)
    rightEar=leftEar.clone()
    rightEar.move(300,0)
    rightEar.draw(win)
    #face
    face=Oval(Point(100,50),Point(400,450))
    face.setFill("Cyan")
    face.draw(win)
    #hair
    mohawk=Rectangle(Point(220,25),Point(280,100))
    mohawk.setFill("maroon")
    mohawk.draw(win)
    #eyes
    leftEye=Circle(Point(175,200),50)
    leftEye.setFill("white")
    leftEye.draw(win)
    leftPupil=Circle(Point(175,200),20)
    leftPupil.setFill("black")
    leftPupil.draw(win)
    rightEye=leftEye.clone()
    rightEye.move(150,0)
    rightEye.draw(win)
    rightPupil=leftPupil.clone()
    rightPupil.move(150,0)
    rightPupil.draw(win)
    #nose
    nose=Polygon(Point(250,150),Point(300,275),Point(200,275))
    nose.setFill("cyan")
    nose.draw(win)
    #mouth
    mouth=Oval(Point(350,370),Point(150,320))
    mouth.setFill("black")
    mouth.draw(win)
    leftTooth=Rectangle(Point(250,370),Point(215,320))
    leftTooth.setFill("white")
    leftTooth.draw(win)
    rightTooth=leftTooth.clone()
    rightTooth.move(35,0)
    rightTooth.draw(win)
    win.getMouse()

main()