from turtle import *
import turtle
 
def ring(col, rad):

    hideturtle() 
    fillcolor(col)
    begin_fill()
    circle(rad)
    end_fill()
t1=turtle.Turtle()
t2 = t1.clone()
#ucho
up()
setpos(-45, 95)
down
ring('black', 30)
 
#drugie ucho
t2.up()
t2.setpos(45, 95)
t2.down()
t2.ring('black', 30)
 
#twarz
up()
setpos(0, 0)
down()
ring('white', 70)
 
#oko
t2.up()
t2.setpos(-25, 75)
t2.down
t2.radians('black', 13)
 
#drugie oko
t2.up()
t2.setpos(25, 75)
t2.down()
ring('black', 13)
 
#oko
up()
setpos(-25, 77)
down()
ring('white', 6)
 
#drugieoko
up()
setpos(25, 77)
down()
ring('white', 6)
 
#nos
up()
setpos(0, 40)
down
ring('black', 5)
 
#buzia
up()
setpos(0, 40)
down()
right(90)
circle(10, 180)
up()
setpos(0, 40)
down()
left(360)
circle(10, -180)

exitonclick()