import turtle
from itertools import cycle

colors = cycle(['red','orange','yellow','green','blue','purple'])

def draw_circle(size):
    turtle.pencolor(next(colors))
    turtle.circle(size)
    turtle.turn(72)
    size = size + 5
    


turtle.bgcolor('black')
turtle.speed('fast')
turtle.pensize(4)
draw_circle(30)
