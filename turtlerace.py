from turtle import *
from random import randint

speed(1000)
penup()
goto(-140, 140)

for step in range (16):
  write(step, align="center")
  right(90)
  forward (10)
  pendown()
  forward(150)
  penup()
  backward(160)
  left(90)
  forward(20)

ton = Turtle()
ton.color ('red')
ton.shape ('turtle')

ton.penup()
ton.goto(-160,100)
ton.pendown()

bob = Turtle()
bob.color ('blue')
bob.shape ('turtle')

bob.penup()
bob.goto(-160,80)
bob.pendown()

speed(100)

for turn in range(105):
    ton.forward(randint(1,5))
    bob.forward(randint(1,5))

