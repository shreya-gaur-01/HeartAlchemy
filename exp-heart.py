import turtle
import math
import random

screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.pensize(1)

colors = ["green","pink", "lightgreen",
          "green","pink", "lightgreen"]

for i in range(120):
    angle = i * (math.pi * 2) / 120

    x = 16 * (math.sin(angle) ** 3) * 15
    y = (13 * math.cos(angle)
         - 5 * math.cos(2 * angle)
         - 2 * math.cos(3 * angle)
         - math.cos(4 * angle)) * 15

    t.penup()
    t.goto(0, 40)
    t.pendown()

    t.color(random.choice(colors))
    t.goto(x, y)

    for _ in range(8):
        t.forward(6)
        t.backward(6)
        t.right(45)

turtle.done()
