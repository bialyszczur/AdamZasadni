from turtle import *

color('green')
bgcolor('black')

speed(10)
penup()
goto(0,100)
pendown()
hideturtle()

b = 0
while b < 200:
    right(b)
    forward(b * 3)
    b = b + 1

exitonclick()