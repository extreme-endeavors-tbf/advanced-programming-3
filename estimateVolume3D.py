from vpython import *
import random

#Global measurements
radius = random.randint(10,200)
length = random.randint(10,200)
width = random.randint(10,200)
height = random.randint(10,200)

#Color and opacity of outside shape
outsideColor = color.blue
outsideOpacity = 0.5

#Color and opacity of inside shape
insideColor = color.green
insideOpacity = 0.5

#Color and opacity of points
pointColor = color.red

def drawSphere(sphereLocation, rad, col, op):
    sphere(pos=sphereLocation, radius=rad, color=col, opacity=op)
    volume = (4/3)*pi*(rad**3)
    return volume

def drawCube(cubeLocation, length, col, op):
    #the dimensions of the cube are in the form of width, height, depth
    dim = vector(length, length, length)
    box(pos=cubeLocation, size=dim, color=col, opacity=op)
    volume = length**3
    return volume

def drawRectPrism(prismLocation, l, w, h, col, op):
    dim = vector(w,h,l)
    box(pos=prismLocation, size=dim, color=col, opacity=op)
    volume = l*w*h
    return volume

def drawOuterShape():
    shapes = ["sphere", "cube", "rectangular prism"]
    randChoice = random.choice(shapes)

    if randChoice == "sphere":
        sphereLocation = vector(0,0,0)
        sphere = drawSphere(sphereLocation,radius,outsideColor,outsideOpacity)
        return randChoice, sphere

    if randChoice == "cube":
        cubeLocation = vector(0,0,0)
        cube = drawCube(cubeLocation, length, outsideColor, outsideOpacity)
        return randChoice, cube

    if randChoice == "rectangular prism":
        prismLocation = vector(0,0,0)
        rectPrism = drawRectPrism(prismLocation,length,width,height,outsideColor,outsideOpacity)
        return randChoice, rectPrism

def drawInnerShape(outsideShape):
    shapes = ["sphere", "cube", "rectangular prism"]
    randChoice = random.choice(shapes)

    if outsideShape[0] == "sphere":
        if randChoice == "sphere":
            sphereLocation = vector(0, 0, 0)
            newRadius = random.randint(1, radius)
            drawSphere(sphereLocation, newRadius, insideColor, insideOpacity)
            return randChoice, newRadius
        if randChoice == "cube":
            cubeLocation = vector(0, 0, 0)
            newLength = random.randint(1,radius)
            drawCube(cubeLocation,newLength,insideColor,insideOpacity)
            return randChoice, newLength
        if randChoice == "rectangular prism":
            prismLocation = vector(0,0,0)
            newLength = random.randint(1, radius)
            newWidth = random.randint(1, radius)
            newHeight = random.randint(1, radius)
            drawRectPrism(prismLocation,newLength,newWidth,newHeight,insideColor,insideOpacity)
            return randChoice, newLength, newWidth, newHeight

    if outsideShape[0] == "cube":
        if randChoice == "sphere":
            sphereLocation = vector(0,0,0)
            newRadius = random.randint(1,length//2)
            drawSphere(sphereLocation,newRadius,insideColor,insideOpacity)
            return randChoice, newRadius
        if randChoice == "cube":
            cubeLocation = vector(0,0,0)
            newLength = random.randint(1,length)
            drawCube(cubeLocation,newLength,insideColor,insideOpacity)
            return randChoice, newLength
        if randChoice == "rectangular prism":
            prismLocation = vector(0,0,0)
            newLength = random.randint(1,length)
            newWidth = random.randint(1,length)
            newHeight = random.randint(1,length)
            drawRectPrism(prismLocation,newLength,newWidth,newHeight,insideColor,insideOpacity)
            return randChoice, newLength, newWidth, newHeight

    if outsideShape[0] == "rectangular prism":
        if randChoice == "sphere":
            sphereLocation = vector(0,0,0)
            minMeasure = min(length, width, height)
            newRadius = random.randint(1,minMeasure//2)
            drawSphere(sphereLocation,newRadius,insideColor,insideOpacity)
            return randChoice, newRadius
        if randChoice == "cube":
            cubeLocation = vector(0,0,0)
            minMeasure = min(length,width,height)
            newLength = random.randint(1,minMeasure)
            drawCube(cubeLocation,newLength,insideColor,insideOpacity)
            return randChoice, newLength
        if randChoice == "rectangular prism":
            prismLocation = vector(0,0,0)
            newLength = random.randint(1,length)
            newWidth = random.randint(1,width)
            newHeight = random.randint(1,height)
            drawRectPrism(prismLocation,newLength,newWidth,newHeight,insideColor,insideOpacity)
            return randChoice, newLength, newWidth, newHeight

def plotPoints(outsideShape,insideShape):
    numOfPoints = random.randint(1,1000)
    print("Number of points:",numOfPoints)

    outsideShapeVolume = outsideShape[1]
    print("The volume of the outside shape is:", outsideShapeVolume)

    listOfPoints = []

    innerShapePoints = 0

    for i in range(numOfPoints):
        if outsideShape[0] == "sphere":
            x = random.randint(-radius // 2, radius // 2)
            y = random.randint(-radius // 2, radius // 2)
            z = random.randint(-radius // 2, radius // 2)
            listOfPoints.append(vector(x,y,z))
            if insideShape[0] == "sphere":
                newRadius = insideShape[1]
                if (x**2) + (y**2) + (z**2) < newRadius**2:
                    innerShapePoints += 1
            if insideShape[0] == "cube":
                newLength = insideShape[1]
                if (x >= -newLength // 2 and x <= newLength // 2) and \
                   (y >= -newLength // 2 and y <= newLength // 2) and \
                   (z >= -newLength // 2 and z <= newLength // 2):
                    innerShapePoints += 1
            if insideShape[0] == "rectangular prism":
                newLength = insideShape[1]
                newWidth = insideShape[2]
                newHeight = insideShape[3]
                if (x >= -newWidth // 2 and x <= newWidth // 2) and \
                   (y >= -newHeight // 2 and y <= newHeight // 2) and \
                   (z >= -newLength // 2 and z <= newLength // 2):
                    innerShapePoints += 1

        if outsideShape[0] == "cube":
            x = random.randint(-length // 2, length // 2)
            y = random.randint(-length // 2, length // 2)
            z = random.randint(-length // 2, length // 2)
            listOfPoints.append(vector(x,y,z))
            if insideShape[0] == "sphere":
                newRadius = insideShape[1]
                if (x**2) + (y**2) + (z**2) < newRadius**2:
                    innerShapePoints += 1
            if insideShape[0] == "cube":
                newLength = insideShape[1]
                if (x >= -newLength // 2 and x <= newLength // 2) and \
                   (y >= -newLength // 2 and y <= newLength // 2) and \
                   (z >= -newLength // 2 and z <= newLength // 2):
                    innerShapePoints += 1
            if insideShape[0] == "rectangular prism":
                newLength = insideShape[1]
                newWidth = insideShape[2]
                newHeight = insideShape[3]
                if (x >= -newWidth // 2 and x <= newWidth // 2) and \
                   (y >= -newHeight // 2 and y <= newHeight // 2) and \
                   (z >= -newLength // 2 and z <= newLength // 2):
                    innerShapePoints += 1

        if outsideShape[0] == "rectangular prism":
            x = random.randint(-width // 2, width // 2) #x corresponds to width
            y = random.randint(-height // 2, height // 2) #y corresponds to height
            z = random.randint(-length // 2, length // 2) #z corresponds to length
            listOfPoints.append(vector(x,y,z))
            if insideShape[0] == "sphere":
                newRadius = insideShape[1]
                if (x**2) + (y**2) + (z**2) < newRadius**2:
                    innerShapePoints += 1
            if insideShape[0] == "cube":
                newLength = insideShape[1]
                if (x >= -newLength // 2 and x <= newLength // 2) and \
                   (y >= -newLength // 2 and y <= newLength // 2) and \
                   (z >= -newLength // 2 and z <= newLength // 2):
                    innerShapePoints += 1
            if insideShape[0] == "rectangular prism":
                newLength = insideShape[1]
                newWidth = insideShape[2]
                newHeight = insideShape[3]
                if (x >= -newWidth // 2 and x <= newWidth // 2) and \
                   (y >= -newHeight // 2 and y <= newHeight // 2) and \
                   (z >= -newLength // 2 and z <= newLength // 2):
                    innerShapePoints += 1

    points(pos=listOfPoints,color=pointColor)
    print(listOfPoints)
    estimatedVolume = outsideShapeVolume * (innerShapePoints / numOfPoints)
    print("Inner shape points:", innerShapePoints)
    print("Estimated volume of the inner shape:", estimatedVolume)

#Main Code
outsideShape = drawOuterShape()
insideShape = drawInnerShape(outsideShape)
plotPoints(outsideShape,insideShape)