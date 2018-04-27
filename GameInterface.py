import turtle
from random import randrange
from turtle import *

CURSOR_SIZE = 20
SQUARE_SIZE = 50
SQUARES_PER_SIDE = 8

#set screen charactersistics
wn=turtle.Screen()
wn.bgcolor('lightblue')
wn.title('Checkers')

#set turtle characteristics
game = turtle.Turtle()
game.speed('fastest')

#draw/fill one square
def square(size,alternate,color):
	game.color(color)
	game.begin_fill()
	for i in range(4):
		game.fd(size)
		game.lt(90)
	game.end_fill()
	game.fd(size)

#draw a row of squares
def row(size,alternate,color1,color2):
	for i in range(4):
		if(alternate==True):
			square(size,alternate,color1)
			square(size,alternate,color2)
		else:
			square(size,alternate,color2)
			square(size,alternate,color1)

#draw the whole checkerboard
def checkerboard(size,alternate,color1,color2):
	game.pu()
	game.goto(-(size*4),(size*4))
	for i in range(8):
		row(size, alternate, color1, color2)
		game.bk(size*8)
		game.rt(90)
		game.fd(size)
		game.lt(90)
		if(alternate==True):
			alternate=False
		else:
			alternate=True

#initialize game board draw to the base game state			
checkerboard(50, True, 'gray', 'white')

#create the 12 red pieces
red_checkers = []
for _ in range(12):
    checker = Turtle('circle')
    checker.color('black', 'red')
    checker.shapesize(SQUARE_SIZE / CURSOR_SIZE)
    checker.penup()
    
    red_checkers.append(checker)
    
#place red pieces in starting position
red_checkers[0].setpos(-125, 225)
red_checkers[1].setpos(-25, 225)
red_checkers[2].setpos(75, 225)
red_checkers[3].setpos(175, 225)
red_checkers[4].setpos(-175, 175)
red_checkers[5].setpos(-75, 175)
red_checkers[6].setpos(25, 175)
red_checkers[7].setpos(125, 175)
red_checkers[8].setpos(-125, 125)
red_checkers[9].setpos(-25, 125)
red_checkers[10].setpos(75, 125)
red_checkers[11].setpos(175, 125)

#create the 12 black pieces
black_checkers = []
for _ in range(12):
    checker = Turtle('circle')
    checker.color('black', 'black')
    checker.shapesize(SQUARE_SIZE / CURSOR_SIZE)
    checker.penup()
    
    black_checkers.append(checker)
    
#place the black pieces in starting position
black_checkers[0].setpos(-175, -125)
black_checkers[1].setpos(-75, -125)
black_checkers[2].setpos(25, -125)
black_checkers[3].setpos(125, -125)
black_checkers[4].setpos(-125, -75)
black_checkers[5].setpos(-25, -75)
black_checkers[6].setpos(75, -75)
black_checkers[7].setpos(175, -75)
black_checkers[8].setpos(-175, -25)
black_checkers[9].setpos(-75, -25)
black_checkers[10].setpos(25, -25)
black_checkers[11].setpos(125, -25)

					
					
				
			
	
	
turtle.mainloop()
