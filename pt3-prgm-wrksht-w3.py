# basic: function one
# the drawStickFigure function in the pract3.py file is incomplete, finish it by drawing the arms and legs

from graphics import *

def drawStickFigure():
    win = GraphWin("Stick figure")
    win.setBackground('black')
    
    head = Circle(Point(100, 60), 20)
    head.setFill('red')
    head.draw(win)
    
    body = Line(Point(100, 80), Point(100, 120))
    body.setFill('red')
    body.draw(win)
    
    leftArm = Line(Point(100, 90), Point(80, 100))
    leftArm.setFill('red')
    leftArm.draw(win)
    
    rightArm = Line(Point(100, 90), Point(120, 100))
    rightArm.setFill('red')
    rightArm.draw(win)
    
    leftLeg = Line(Point(100, 120), Point(80, 150))
    leftLeg.setFill('red')
    leftLeg.draw(win)
    
    rightLeg = Line(Point(100, 120), Point(120, 150))
    rightLeg.setFill('red')
    rightLeg.draw(win)
    
    win.getMouse()
    win.close()

drawStickFigure()

# basic: second function 
# write a drawCircle function which asks the user for the radius of a circle and then draws the circle in the centre of a graphics window

from graphics import *

def drawCircle():
    win = GraphWin("Draw Circle", 400, 400)
    win.setBackground('black')

    radius = float(input("Enter the radius of the circle: "))

    centerX = win.getWidth() // 2
    centerY = win.getHeight() // 2

    circle = Circle(Point(centerX, centerY), radius)
    circle.setFill('pink')
    circle.setOutline('white')
    circle.draw(win)

    win.getMouse()
    win.close()

drawCircle()

# basic: third function
# write a drawArcheryTarget function that draws a target made of yellow, red, and blue circles, the sizes of the circles should be in correct proportion,
# i.e. the red circle should have a radius twice that of the yellow circle, and the blue circle should have a radius three times that of the yellow circle

from graphics import *

def drawArcheryTarget():
    win = GraphWin("Archery Target", 400, 400)
    win.setBackground('black')
    
    blueCircle = Circle(Point(200, 200), 99.99)
    blueCircle.setFill('blue')
    blueCircle.draw(win)

    redCircle = Circle(Point(200, 200), 66.66)
    redCircle.setFill('red')
    redCircle.draw(win)

    yellowCircle = Circle(Point(200, 200), 33.33)
    yellowCircle.setFill('yellow')
    yellowCircle.draw(win)

    win.getMouse()
    win.close()

drawArcheryTarget()

# basic: fourth function
# Write a drawRectangle function which asks the user for the height and width of a rectangle first, 
# your function should draw the rectangle in the centre of a graphics window of size 200 × 200,
# there should be equal spaces to the left and right, and above and below the rectangle, assume that the user enters values less than 200

from graphics import *

def drawRectangle():
    win = GraphWin("Draw Rectangle", 200, 200) 
    win.setCoords(0, 0, 200, 200) 

    height = float(input("Enter the height of the rectangle (less than 200): "))
    width = float(input("Enter the width of the rectangle (less than 200): "))

    leftX = (200 - width) / 2
    rightX = leftX + width
    topY = (200 - height) / 2
    bottomY = topY + height

    rect = Rectangle(Point(leftX, topY), Point(rightX, bottomY))
    rect.setFill('red')
    rect.draw(win)

    win.getMouse()
    win.close()

drawRectangle()

# basic: fifth function
# write a blueCircle function that allows the user to draw a blue circle of radius 50 by clicking on the location of the circle’s centre

from graphics import *

def blueCircle():
    win = GraphWin("Blue Circle", 400, 400)

    instructions = Text(Point(200, 20), "Click to place a blue circle with radius 50")
    instructions.setOutline('white')
    instructions.draw(win)

    center = win.getMouse()

    centerX = center.getX()
    centerY = center.getY()

    circle = Circle(center, 50)
    circle.setFill("blue")
    circle.setOutline("black")
    circle.draw(win)

    win.getMouse()
    win.close()

blueCircle()

# basic: sixth function
# The function drawLine in the pract3.py file allows the user to draw a line by choosing two points, 
# notice how we use the getMouse function to get the Point from the user 
# write a function tenLines that allows the user to draw 10 such lines

from graphics import *

def drawLines():
    win = GraphWin("Line Drawer", 400, 400)
    message = Text(Point(100, 380), "Click on the first point")
    message.draw(win)

    for i in range(10): 
        p1 = win.getMouse()
        message.setText("Click on the second point")
        p2 = win.getMouse()
        line = Line(p1, p2)
        line.draw(win)
        message.setText("")

    message.setText("All lines drawn. Click to close the window.")
    win.getMouse()
    win.close()

drawLines()

# basic: seventh function 
# write a tenStrings function which allows the user to plot 10 strings of their choice at locations of a graphics window chosen by clicking on the mouse, 
# (the strings should be entered one-by-one by the user within a text entry box at the top of the graphics window, 
# clicking the mouse after entering each one

from graphics import *

def tenStrings():
    win = GraphWin("String Plotter", 400, 400)
    win.setBackground('white')
    
    entryBox = Entry(Point(200, 380), 40)
    entryBox.draw(win)
    entryLabel = Text(Point(200, 360), "Enter a string:")
    entryLabel.draw(win)
    
    strings = [] 
    
    for x in range(10):
        entryBox.setText("")  
        entryBox.setTextColor("black")  
        entryLabel.setText("Enter a string ({} remaining):".format(10 - len(strings)))
      
        win.getMouse()
        userInput = entryBox.getText()
        
        strings.append(userInput)
    
        text = Text(win.getMouse(), userInput)
        text.draw(win)
    
    entryLabel.setText("All strings entered. Click to close the window.")
    
    win.getMouse()
    win.close()

tenStrings()

# basic: eighth function
# write a tenColouredRectangles function to allow the user to draw 10 coloured rectangles on the screen, 
# the user should pick the coordinates of the top-left and bottom-right corners of every rectangle by clicking on the window
# the user needs to select the colour of each rectangle by entering a colour, for example blue, in a provided entry box at the top of the window, 
# (the colour of each rectangle is given by the string that is in this box when the user clicks its bottom-right point) 
# the entry box should initially contain the string "blue", assume that the user never enters an invalid colour into the entry box

from graphics import *

def tenColouredRectangles():

    win = GraphWin("Ten Coloured Rectangles", 400, 400)
    win.setBackground('white')

    colorEntry = Entry(Point(200, 20), 10)
    colorEntry.setText("blue")
    colorEntry.draw(win)

    colorLabel = Text(Point(100, 20), "Enter Color:")
    colorLabel.draw(win)

    rectangles = []

    for _ in range(10):
        color = colorEntry.getText()

        topLeft = win.getMouse()
        bottomRight = win.getMouse()

        rectangle = Rectangle(topLeft, bottomRight)
        rectangle.setFill(color)
        rectangle.draw(win)

        rectangles.append(rectangle)

    win.getMouse()
    win.close()

if __name__ == "__main__":
    tenColouredRectangles()

# harder: ninth function
# write a fiveClickStickFigure function that allows the user to draw a (symmetric) stick figure in a graphics window, 
# using five clicks of the mouse to determine the positions of its features, as illustrated in the figure below, 
# each feature should be drawn as the user clicks the points
# hint: the radius of the head is the distance between points 1 and 2 — see the previous worksheet, 
# note that only the y-coordinate of point 3 should be used—its x-coordinate should be copied from point 1

from graphics import *

def fiveClickStickFigure():

    win = GraphWin("Stick Figure", 400, 400)

    points = [win.getMouse() for _ in range(5)]

    headRadius = points[1].getY() - points[0].getY()

    headCenter = points[0]
    head = Circle(headCenter, headRadius)
    head.setFill("yellow")
    head.draw(win)

    body = Line(Point(headCenter.getX(), headCenter.getY() + headRadius), points[3])
    body.setWidth(3)
    body.draw(win)

    leftArm = Line(points[3], points[4])
    leftArm.setWidth(3)
    leftArm.draw(win)

    rightArm = Line(points[3], Point(points[2].getX(), points[4].getY()))
    rightArm.setWidth(3)
    rightArm.draw(win)

    leftLeg = Line(points[3], Point(points[1].getX(), points[3].getY() + headRadius * 2))
    leftLeg.setWidth(3)
    leftLeg.draw(win)

    rightLeg = Line(points[3], Point(points[2].getX(), points[3].getY() + headRadius * 2))
    rightLeg.setWidth(3)
    rightLeg.draw(win)

    win.getMouse()
    win.close()

if __name__ == "__main__":
    fiveClickStickFigure()

    