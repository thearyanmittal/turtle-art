from turtle import *

home()
clear()
hideturtle()
speed(0)
colormode(255)

def polygon(length, angle, step):
    for i in range(step):
        pencolor(0, i, 255-i)
        for b in range(2):
            side = length + i*2
            forward(side)
            right(angle+b)
    for j in range(step):
        pencolor(0, 255-j, j)
        for c in range(2):
            forward(side-j*2)
            right(angle+c)


#pencolor('black')
polygon(50, 90, 255)
exitonclick()