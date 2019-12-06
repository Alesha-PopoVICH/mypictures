import turtle
import math
from turtle import *


def romb(x, y, size, color, angle):
    angle = math.radians(angle)
    t = Turtle()
    size_x = 2*(abs(x)+2*abs(size*math.cos(angle/2)))+50
    size_y = 2*(abs(y)+abs(size*math.sin(angle/2)))+50
    scale = min(800/size_x, 800/size_y)
    t.screen.setup(800, 800)
    t.pencolor(color)
    t.ht()
    t.penup()
    t.goto(scale*x, scale*y)
    t.pendown()
    t.goto(scale*(x+size*math.cos(angle/2)), scale*(y+size*math.sin(angle/2)))
    t.goto(scale*(x+2*size*math.cos(angle/2)), scale*y)
    t.goto(scale*(x+size*math.cos(angle/2)), scale*(y-size*math.sin(angle/2)))
    t.goto(scale*x, scale*y)
    t.screen.exitonclick()
    t.screen.mainloop()
    
romb(-900, 900, 1350, 'red', 130)

from turtle import *
import random as r
t = Turtle()
t.screen.setup(800, 800)
a = 0
b = 0
col = ["red", "blue", "green", "cyan", "purple"]
def coord():
    global a
    global b
    a = r.randint(-200, 200)
    b = r.randint(-200, 200)
def flower(x, y, color):
    t.up()
    t.goto(x, y - 200)
    t.setheading(90)
    t.color("green")
    t.down()
    t.fd(200)
    t.setheading(0)
    t.color("yellow")
    t.begin_fill()
    t.fillcolor("yellow")
    t.circle(20, 360)
    t.end_fill()
    for i in range(4):
        t.color(color)
        t.begin_fill()
        t.circle(-35, 360)
        t.end_fill()
        t.color("yellow")
        t.circle(20, 90)
t.speed(0)
for i in range(5):
    coord()
    flower(a, b, col[i])
t.screen.exitonclick()
t.screen.mainloop()
