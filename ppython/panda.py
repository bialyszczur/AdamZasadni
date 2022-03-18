from turtle import *

def pand(col, rad):
    hideturtle()
    fillcolor(col)
    begin_fill()
    circle(rad)
    end_fill()

up()
goto(-45,95)
down()
pand('black', 30)
up()
goto(45,95)
down()
pand('black', 30)

up()
goto(0,0)
down()
pand('white', 70)

up()
goto(-25, 75)
down()
pand('black', 13)
up()
goto(25, 75)
down()
pand('black', 13)

up()
goto(-25,77)
down()
pand('white', 6)
up()
goto(25, 77)
down()
pand('white', 6)

up()
goto(0, 40)
down()
pand('black', 5)

up()
goto(0, 40)
down()
right(90)
circle(10, 180)
up()
goto(0, 40)
down()
left(360)
circle(10, -180)

exitonclick()






































































