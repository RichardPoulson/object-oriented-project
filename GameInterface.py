
import turtle

#set screen charactersistics
wn=turtle.Screen()
wn.bgcolor('lightblue')
wn.title('Checkers')

#set turtle characteristics
game = turtle.Turtle()
game.speed(0)

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
			
checkerboard(50, True, 'gray', 'white')
turtle.mainloop()
