from turtle import *

title("DAWAJ MI PIWO")

def drag(i, j):
    tur.ondrag(None)
    tur.setheading(tur.towards(i, j))
    tur.goto(i, j)
    tur.ondrag(drag)

ws = Screen()

tur = Turtle('turtle')
tur.speed('fastest')

tur.ondrag(drag)

ws.mainloop()