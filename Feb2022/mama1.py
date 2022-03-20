for counter in range(1,11):
    print('Emma\'s Room - Keep Out!!!')

hippos = 0
answer = 'y'
while answer == 'y':
    hippos = hippos + 1
    print(str(hippos) + ' balancing hippos!')
    answer = input('Add another hippo? (y/n)')




import turtle as t
def rectangle(horizontal, vertical, color):
    t.pendown()
    t.pensize(1)
    t.color(color)
    t.begin_fill()
    for counter in range(1,3):
        t.forward(horizontal)
        t.right(90)
        t.forward(vertical)
        t.right(90)
    t.end_fill()
    t.penup()
    t.speed('slow')
    t.bgcolor('Dodger blue')
    t.goto(-100,-150)
    rectangle(50,20,'blue')
    t.goto(-30,-150)
    rectangle(50,20,'blue') 
    t.goto(-25,-50)
    rectangle(15,100,'grey') 
    t.goto(-55,-50)
    rectangle(-15,100,'grey')
    t.goto(-90,100)
    rectangle(100,150,'red')  
    t.goto(-150,-70)
    rectangle(60,15,'grey') 
    t.goto(-150,110)
    rectangle(15,40,'grey') 

    t.goto(10,70)
    rectangle(60,15,'grey') 
    t.goto(55,110)
    rectangle(15,40,'grey') 
    t.goto(-50,120)
    rectangle(15,20,'grey') 
    t.goto(-85,170)
    rectangle(80,50,'red') 
    t.goto(-25,-50)
    rectangle(30,10,'white') 
    t.goto(-55,155)
    rectangle(5,5,'black') 
    t.goto(-40,155)
    rectangle(15,100,'black') 
    t.goto(-65,135)
    rectangle(40,5,'black') 
    t.hideturtle()

import turtle as t
t.fillcolor("yellow" )
t.begin_fill()
for _ in range(5):
    t.forward(200)
    t.left(72)
t.end_fill()
t.fillcolor("red")
t.begin_fill()
for _ in range(82):
    t.forward(10)
    t.left(4)
t.end_fill()
t.fillcolor("blue" )
t.begin_fill()
for _ in range(4):
    t.forward(200)
    t.left(90)
t.end_fill()
t.fillcolor("grey" )
t.begin_fill()
for _ in range(3):
    t.forward(120)
    t.left(120)
t.left(240)
t.end_fill()
t.fillcolor("purple" )
t.begin_fill()
for _ in range(12):
    t.forward(10)
    t.left(30)
t.end_fill()
t.fillcolor("pink" )
t.begin_fill()
for _ in range(5):
    t.forward(10)
    t.left(36)
    t.forward(10)
    t.left(72)
t.end_fill()


import turtle
from itertools import cycle

colors = cycle(['red','orange','yellow','green','blue','purple'])

def draw_circle(size):
    turtle.pencolor(next(colors))
    turtle.circle(size)
    draw_circle(size+5)


turtle.bgcolor('black')
turtle.speed('fast')
turtle.pensize(4)
draw_circle(30)

