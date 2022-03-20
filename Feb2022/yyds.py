import turtle
t = turtle.Pen()
sides= 100
colors=["red","yellow","green","blue","orange","purple"]
for x in range(360):
    t.pencolor(colors[x%sides])
    t.forward(x)
    t.left(59)

#SquareSpiral1.py
import turtle
t = turtle.Pen()
turtle.bgcolor("black")
sides= 100
colors=["red","yellow","green","blue","orange","purple"]
for x in range(360):
    t.pencolor(colors[x%sides])
    t.forward(x*3/sides+x)
    t.left(360/sides+1)
    t.width(x*sides/200)


print("####结束####")

import turtle
t = turtle.Pen()
sides= 100
colors=["red","yellow","green","blue","orange","purple"]
for x in range(360):
    t.pencolor(colors[x%sides])
    t.forward(x)
    t.left(59)

