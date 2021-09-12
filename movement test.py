from turtle import *
from random import randint

speed (100)
goto(randint(-100,100),randint(-100,100))
pendown()

for step in range(1000):
    forward(randint(10,100))
    right(randint(-360,360))
