# first: graphic function
# simply draw a 500x500 window using Graphics.py

from graphics import *

def frst():
    win = GraphWin("My window", 500, 500)
    win.getMouse()
    win.close()
frst()

from graphics import *

# next: ask user for dimensions (width, height) then draw a with these width and height dimensions

def frstNxt():
    usrInptW = int(input("Enter the dimensions of the window width: "))
    usrInptH = int(input("Enter the dimensions of the window height: "))
    win = GraphWin("My window", usrInptW, usrInptH)
    win.getMouse()
    win.close()
frstNxt()
 
# second: graphic function
# simply draw a 100x100 rectangle on a window using Graphics.py

from graphics import *

def rect1():
    win = GraphWin("My Window", 300, 300)
    win.setBackground('white')

    aR = Rectangle(Point(50, 50), Point(150, 150))
    aR.setFill('red')
    aR.draw(win)

    win.getMouse()
    win.close()
rect1()

# next: ask user for dimensions of rectangle then draw a with these width and height dimensions

from graphics import *

def rect2():
    win = GraphWin("My Window", 500, 500)
    win.setBackground('grey')

    usrInptX1 = int(input("Please enter the x1 value: "))
    usrInptX2 = int(input("Please enter the x2 value: "))
    usrInptY1 = int(input("Please enter the y1 value: "))
    usrInptY2 = int(input("Please enter the y2 value: "))

    rec = Rectangle(Point(usrInptX1, usrInptX2), Point(usrInptY1, usrInptY2))
    rec.setFill('white')
    rec.draw(win)

    win.getMouse()
    win.close()
rect2()

# third: graphic function
# draw window, then rectangle, then click window and move rectangle to this location

from graphics import *

def rectM():
    win = GraphWin("Move Rectangle", 400, 400)
    win.setBackground('grey')

    rectWidth = 60
    rectHeight = 40
    rect = Rectangle(Point(170, 180), Point(230, 220))
    rect.setFill("blue")
    rect.draw(win)

    while True:
        clickPoint = win.getMouse()
        rectCenter = rect.getCenter()

        new_x = clickPoint.getX() - (rectWidth / 2)
        new_y = clickPoint.getY() - (rectHeight / 2)

        rect.move(new_x - rectCenter.getX(), new_y - rectCenter.getY())

    win.close()

if __name__ == "__main__":
    rectM()

# variation: click window then change colour

from graphics import *

def rectCC():
    win = GraphWin("Change Rectangle Color", 400, 400)

    rect = Rectangle(Point(150, 150), Point(250, 250))
    rect.setFill("blue")
    rect.draw(win)

    while True:
        clickPoint = win.getMouse()

        colours = ["red", "green", "blue", "yellow", "purple", "orange"]
        newColour = colours[int(clickPoint.getX()) % len(colours)]
        rect.setFill(newColour)

        win.getMouse()

if __name__ == "__main__":
    rectCC()

# variation: click window then move the rectangle down the screen for every click

from graphics import *

def main():
    win = GraphWin("Move Rectangle Down", 400, 400)
    win.setBackground('white')

    rectWidth = 60
    rectHeight = 40
    rect = Rectangle(Point(170, 50), Point(230, 90))
    rect.setFill('black')
    rect.draw(win)

    while True:
        clickPoint = win.getMouse()

        newX1 = rect.getP1().getX()
        newY1 = rect.getP1().getY() + rectHeight
        newX2 = rect.getP2().getX()
        newY2 = rect.getP2().getY() + rectHeight

        rect.undraw()  
        rect = Rectangle(Point(newX1, newY1), Point(newX2, newY2))
        rect.setFill('black')
        rect.draw(win)

if __name__ == "__main__":
    main()

