'''
I originally created this game using PyGame, but I had trouble figuring out how to
handle the dependencies in my PyGame so that when someone else loads it in their machine,
they don't have to download PyGame to make it work. I tried multiple things, it took me all
weekend. With that being said, I now give you the turtle version of the game.
'''
import turtle
from random import randint

#Create window
screen = turtle.Screen()
screen.setup(1200,772)
screen.bgpic('serengeti.gif')
screen.addshape('player.gif')
screen.addshape('lion.gif')

#Create player & place it somewhere on the screen using randint()
player = turtle.Turtle()
player.penup()
player.setx(randint(-300,300))
player.sety(randint(-300,0))
player.shape('player.gif')

#Create lion & place it somewhere on the screen using randint()
lion = turtle.Turtle()
lion.penup()
lion.setx(randint(-400,400))
lion.sety(randint(-300,0))
lion.shape('lion.gif')

#Player speed
speed = 100

#Game functions
def writeDirections():
    pen = turtle.Turtle()
    pen.penup()
    pen.setx(-500)
    pen.sety(250)
    pen.write("Directions: Use Arrow Keys to Move Player", font=("Calibri", 32, "bold"))
    pen.sety(pen.ycor()-50)
    pen.write("Press 'c' to catch the lion", font=("Calibri", 32, "bold"))

def moveDown():
    player.setheading(270)
    player.forward(speed)

def moveUp():
    player.setheading(90)
    player.forward(speed)

def moveLeft():
    player.setheading(0)
    player.back(speed)

def moveRight():
    player.setheading(0)
    player.forward(speed)

def victory():
    #Clear the player and lion from the game
    player.hideturtle()
    lion.hideturtle()

    #Create new screen for the victory image
    victoryScreen = turtle.Screen()
    victoryScreen.setup(500,500)
    victoryScreen.bgpic('victory.gif')

def catchTheLion():
    #Check to see if the coordinates of the player and the lion are within
    #20 degrees of each other
    xDiff = abs(player.xcor() - lion.xcor())
    yDiff = abs(lion.ycor() - lion.ycor())

    if xDiff <= 20 and yDiff <= 20:
        victory()

#Set keyboard commands
turtle.listen()
screen.onkey(moveUp, "Up")
screen.onkey(moveDown, "Down")
screen.onkey(moveLeft, "Left")
screen.onkey(moveRight, "Right")
screen.onkey(catchTheLion, "c")

#Write the commands on the screen for the user
writeDirections()

#This loop is where we make the lion run around the screen
while True:
    lion.setx(randint(-400, 400))
    lion.sety(randint(-300, 0))

#Exit on click
screen.exitonclick()