import turtle
import random

def drawLine(): #function that draws the line for bisection
    turtle.back(50)
    turtle.pencolor("red")
    turtle.pendown()
    turtle.forward(200)
    turtle.penup()

def drawTriangle():
    angleA = random.uniform(0.0,180.0)
    print(angleA)

    turtle.forward(100)
    turtle.left(180 - angleA)

    turtle.forward(100)

    turtle.home()
    turtle.penup()

    turtle.forward(100)
    turtle.left((180-angleA) + (angleA / 2))
    drawLine()

    angleB = (180 - angleA) / 2
    print(angleB)
    turtle.back(150)
    turtle.right(angleA / 2)
    turtle.forward(100)
    turtle.left((180 - angleB) + (angleB / 2))
    drawLine()

    angleC = 180 - angleA - angleB
    print(angleC)
    turtle.back(150)
    turtle.home()
    turtle.left((angleC / 2))
    drawLine()

#Driver code for triangles
while(True):
    drawTriangle()
    turtle.home()
    turtle.color("black")
    turtle.pendown()
    turtle.clear()

turtle.Screen().exitonclick()