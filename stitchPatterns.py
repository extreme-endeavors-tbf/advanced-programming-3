import tkinter as tk
from tkinter import *
from random import randint

def getVersion():
    #User gets the option to create their own pattern or have one generated
    version = input("If you want the randomized version, type 'RANDOM' "
                    "If you want to try different inputs, type 'INPUTS': ")

    return version

def getInput():
    '''
        Get user input for horizontal statement and vertical statement.
        The horizontal parm will be a string and the vertical parm will
        be a number whose length should equal the same length of the string.
    '''
    horizontalInput = input("Enter a phrase (ex: movie quote, name, song lyrics, mantra, etc.): ")
    noSpaces = ""
    for i in range(len(horizontalInput)):
        if horizontalInput[i] != " ":
            noSpaces += horizontalInput[i]
    horizontalInput = noSpaces.lower()
    print(horizontalInput)

    verticalInput = input("Enter a sequence of digits (no commas or spaces allowed): ")
    print(verticalInput)

    '''
        For visual purposes, the length of horizontal input must be the same
        length as the vertical input. If they aren't the same length, then
        the picture will not look right.
    '''
    if len(horizontalInput) != len(verticalInput):
        print("Both inputs must be of the same length")
        return None

    return horizontalInput, verticalInput

def generateNumbers(horizontalInput, verticalInput):
    #set up the vertical and horizontal numbers
    horizontalNumbers = []
    verticalNumbers = []
    '''
        The rule established for horizontal input: if the char in our string is
        a vowel, then that is the dashed line we are going to offset. If not, then
        draw the dashed line as usual.
    '''
    for char in horizontalInput:
        if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
            horizontalNumbers.append(1)
        else:
            horizontalNumbers.append(0)
    '''
        The rule established for vertical input: if the digit is considered to be an
        odd number, then that is the dashed line we are going to offset. If not, then
        draw the dashed line as usual.
    '''
    for digit in verticalInput:
        if int(digit) % 2 != 0:
            verticalNumbers.append(1)
        else:
            verticalNumbers.append(0)

    return horizontalNumbers, verticalNumbers

def generateRandomNumbers():
    # set up the vertical and horizontal numbers
    horizontalNumbers = []
    verticalNumbers = []

    for i in range(1600):
        horizontalNumbers.append(randint(0,2))
        verticalNumbers.append(randint(0,2))

    return horizontalNumbers, verticalNumbers

def dashedHorizontalLine(depth, start, horizontalNumbers):
    '''
        Use for loop to set x and y coordinates for the drawing of the horizontal
        dashed line and draw the line using those x and y coordinates
    '''
    for x in range(0, len(horizontalNumbers) // 2):
        points = [
            start, #x0
            depth, #y0
            start + 10, #x1
            depth #y1
        ]
        canvas.create_line(points, fill="black", width=2)
        '''
            This is used to create the "dashed" part by setting the start tobe significantly
            farther apart from the end of the preceding solid black line
        '''
        start = start + 20

def dashedVerticalLine(depth, start, verticalNumbers):
    '''
        Use for loop to set x and y coordinates for the drawing of the vertical
        dashed line and draw the line using those x and y coordinates
    '''
    for x in range(0, len(verticalNumbers) // 2):
        points = [
            depth, #x0
            start, #y0
            depth, #x1
            start + 10 #y1
        ]
        canvas.create_line(points, fill="black", width=2)
        start = start + 20

def drawPattern(horizontalNumbers, verticalNumbers):
    for index, value in enumerate(verticalNumbers):
        #if we encounter a 0, in the list, do not offset
        if value % 2 == 0:
            dashedVerticalLine(index * 10, 0, verticalNumbers)
        #if we encounter a 1, do offset
        else:
            dashedVerticalLine(index * 10, 10, verticalNumbers)

    for index, value in enumerate(horizontalNumbers):
        if value % 2 == 0:
            dashedHorizontalLine(index * 10, 0, horizontalNumbers)
        else:
            dashedHorizontalLine(index * 10, 10, horizontalNumbers)

#create a new window with tkinter
window = Tk()

#set the title of the window
window.title("Hitomezashi Stitch Patterns")

#set width and height of the window -- full screen mode
window.geometry("1600x1600")

#create canvas to draw the lines
canvas = Canvas(background='white')
canvas.pack(fill=tk.BOTH, expand= True)

#Check to see which version the user entered
version = getVersion()
if version == 'INPUTS':
    #get the phrase and int from the user
    inputs = getInput()
    if inputs == None:
        exit(0) #quit the program if we have input of different lengths
    else:
        #generate numbers for the pattern
        numbers = generateNumbers(inputs[0], inputs[1])
elif version == 'RANDOM':
    print("Please wait while we generate your pattern")
    numbers = generateRandomNumbers()
else:
    print("Invalid version command. Please try again.")
    exit(0)

#draw the stitch pattern on the screen
drawPattern(numbers[0], numbers[1])

#run the main loop for tkinter
mainloop()