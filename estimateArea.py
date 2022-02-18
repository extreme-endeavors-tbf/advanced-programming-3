from turtle import *
from math import *
from random import *

'''
    First, I would like to warn you that there is a bug with calculating the area for the inner
    shape when the inner shape is a circle. I tried many different methods but I had not found
    a good enough solution. Everything else should work as is.
'''

radius = randint(100,501)
length = randint(100,501)
width = randint(100,501)

squareCoors = []
rectCoors = []

def drawCircle(radius):
    circle(radius)
    print("The radius of this circle is:", radius)
    penup()
    areaOfCircle = pi * radius ** 2
    sety(radius)
    origin = position()

    return areaOfCircle, origin

def drawSquare(length):
    print("The length of the square's sides is:", length)
    for i in range(4):
        squareCoors.append(position())
        forward(length)
        left(90)

    penup()
    areaOfSquare = length**2

    return areaOfSquare

def drawRectangle(length,width):
    print("The length of the rectangle is:", length)
    print("The width of the rectangle is:", width)
    for i in range(2):
        rectCoors.append(position())
        forward(length)
        left(90)
        rectCoors.append(position())
        forward(width)
        left(90)

    penup()
    areaOfRectangle = length * width

    return areaOfRectangle

def drawOuterShape():
    outerShape = input("Which shape would you like for the outer shape? -- circle, square, or rectangle? ")
    print("\nThe outer shape that you have chosen is:", outerShape.lower())

    if outerShape.lower() == "circle":
        return outerShape.lower(), drawCircle(radius)

    elif outerShape.lower() == "square":
        return outerShape.lower(), drawSquare(length)

    elif outerShape.lower() == "rectangle":
        return outerShape.lower(), drawRectangle(length,width)

    else:
        print("Invalid command. Please try again.")
        exit(0)

def drawInnerShape(outerShape):
    innerShape = input("\nWhich shape would you like for the inner shape? -- circle, square, or rectangle? ")
    print("\nThe inner shape that you have chosen is:", innerShape.lower())

    if innerShape.lower() == "circle":
        if outerShape == "circle":
            newRadius = randint(0,radius)
            sety(radius - newRadius)

        if outerShape == "square":
            newRadius = randint(50,length//2)
            setx(length//2)

        if outerShape == "rectangle":
            newRadius = randint(50,width//2)
            setx(length // 2)

        pendown()
        circle = drawCircle(newRadius)
        return innerShape.lower(), newRadius, circle[1]

    if innerShape.lower() == "square":
        if outerShape == "circle":
            newLength = randint(50,radius)
            sety(newLength // 2)
            setx(xcor()-(newLength // 2))

        if outerShape == "square":
            newLength = randint(50, length)

        if outerShape == "rectangle":
            if width < length:
                newLength = randint(50,width)
            else:
                newLength = randint(50, length)

        pendown()
        drawSquare(newLength)
        return innerShape.lower(), newLength

    if innerShape.lower() == "rectangle":
        if outerShape == "circle":
            newLength = randint(50,radius)
            newWidth = randint(50, radius)
            if newLength < newWidth:
                sety(newWidth/2)
                setx(xcor()-(newLength // 2))
            else:
                sety(newLength/2)
                setx(xcor() - (newWidth // 2))

        if outerShape == "square":
            newLength = randint(50, length)
            newWidth = randint(50, length)

        if outerShape == "rectangle":
            newLength = randint(50,length)
            newWidth = randint(50, width)

        pendown()
        drawRectangle(newLength, newWidth)
        return innerShape.lower(), newLength, newWidth

    else:
        print("Invalid command. Please try again.")
        exit(0)


def plotRandomPoints(outerShape, innerShape):
    numOfPoints = int(input("\nHow many random points do you want to plot? "))
    color("red")

    innerShapePoints = 0

    if outerShape[0] == "circle":
        print("The area of the outer shape is:", outerShape[1][0])
        origin = outerShape[1][1]
        for i in range(numOfPoints):
            penup()
            goto(origin[0],origin[1])
            left(randint(0, 360))
            forward(randint(0,radius))
            dot()
            if innerShape[0] == "circle":
                setheading(0)
                setx((radius*xcor()) / ycor())
                sety(radius)
                if distance(origin) <= innerShape[1]:
                    innerShapePoints += 1
            if innerShape[0] == "square":
                if xcor() >= squareCoors[0][0] and xcor() <= squareCoors[1][0]:
                    if ycor() >= squareCoors[0][1] and ycor() <= squareCoors[3][1]:
                        innerShapePoints += 1
            if innerShape[0] == "rectangle":
                if xcor() >= rectCoors[0][0] and xcor() <= rectCoors[1][0]:
                    if ycor() >= rectCoors[0][1] and ycor() <= rectCoors[3][1]:
                        innerShapePoints += 1
        estimatedArea = outerShape[1][0] * (innerShapePoints / numOfPoints)
        print("The estimated area of the inner shape is:", estimatedArea)

    if outerShape[0] == "square":
        print("The area of the outer shape is:", outerShape[1])
        for i in range(numOfPoints):
            penup()
            setx(randint(0,length))
            sety(randint(0,length))
            dot()
            if innerShape[0] == "circle":
                origin = innerShape[2]
                setheading(0)
                setx((radius * xcor()) / ycor())
                sety(radius)
                if distance(origin) <= innerShape[1]:
                    innerShapePoints += 1
            if innerShape[0] == "square":
                if xcor() <= innerShape[1] and ycor() <= innerShape[1]:
                    innerShapePoints += 1
            if innerShape[0] == "rectangle":
                if xcor() <= innerShape[1] and ycor() <= innerShape[2]:
                    innerShapePoints += 1
        estimatedArea = outerShape[1] * (innerShapePoints / numOfPoints)
        print("The estimated area of the inner shape is:", estimatedArea)

    if outerShape[0] == "rectangle":
        print("The area of the outer shape is:", outerShape[1])
        for i in range(numOfPoints):
            penup()
            setx(randint(0,length))
            sety(randint(0,width))
            dot()
            if innerShape[0] == "circle":
                origin = innerShape[2]
                setheading(0)
                setx((radius * xcor()) / ycor())
                sety(radius)
                if distance(origin) <= innerShape[1]:
                    innerShapePoints += 1
            if innerShape[0] == "square":
                if xcor() <= innerShape[1] and ycor() <= innerShape[1]:
                    innerShapePoints += 1
            if innerShape[0] == "rectangle":
                if xcor() <= innerShape[1] and ycor() <= innerShape[2]:
                    innerShapePoints += 1
        estimatedArea = outerShape[1] * (innerShapePoints / numOfPoints)
        print("The estimated area of the inner shape is:", estimatedArea)

#Set screen size
screensize(2000,2000)

#Draw shapes
outerShape = drawOuterShape()
innerShape = drawInnerShape(outerShape[0])

#Draw the points and print the calculated area via Monte Carlo
plotRandomPoints(outerShape, innerShape)

done()