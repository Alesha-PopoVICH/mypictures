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
