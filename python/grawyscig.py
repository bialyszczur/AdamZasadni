from turtle import *
from random import *

gracz1 = Turtle()
gracz1.color("green")
gracz1.shape("turtle")
gracz1.penup()
gracz1.goto(-200,100)
gracz2 = gracz1.clone()
gracz2.color("blue")
gracz2.penup()
gracz2.goto(-200,-100)

gracz1.goto(300,60)
gracz1.pendown()
gracz1.circle(40)
gracz1.penup()
gracz1.goto(-200,100)
gracz2.goto(300,-140)
gracz2.pendown()
gracz2.circle(40)
gracz2.penup()
gracz2.goto(-200,-100)

die = [1,2,3,4,5,6]

for i in range(20):
     if gracz1.pos() >= (300,100):
             print("Gracz 1 wygrya!")
             break
     elif gracz2.pos() >= (300,-100):
             print("Gracz 2 wygrywa!")
             break
     else:
             ruchgracza1 = input("Naciśnij 'Enter' żeby rzucić kostką ")
             die_outcome = random.choice(die)
             print("Kostka wyrzuciła: ")
             print(die_outcome)
             print("Liczba kroków to: ")
             print(20*die_outcome)
             gracz1.fd(20*die_outcome)
             ruchgracza2 = input("Naciśnij 'Enter' żeby rzucić kostką ")
             die_outcome = random.choice(die)
             print("Kostka wyrzuciła: ")
             print(die_outcome)
             print("Liczba kroków to: ")
             print(20*die_outcome)
             ruchgracza2.fd(20*die_outcome)