from turtle import *
import random

harry = Turtle()
harry.penup()
harry.goto(0, 0)
harry.setheading(90)
harry.pendown()
harry.clear()
harry.hideturtle()
harry.speed(0)
colormode(255)

length = 100
angle = 15
depth = 10
rad = 150
ext = 15

def tree(radius, extent, depth, turtboi):
    if depth > 0:
        right = turtboi
        right.pensize(depth)
        if depth > 3:
            right.pencolor(79, 30, 26)
        elif depth > 2:
            right.pencolor('#633936')
        else:
            leaf = random.choice(['#C91E0A', '#753a36', '#DF3908', '#EDA421', '#E98604', '#A79F0F', '#8B9216'])
            right.pencolor(leaf)

        left = turtboi.clone()

        right.circle(radius, extent)
        left.circle(-radius, extent)

        tree(radius-1, extent, depth-1, left)
        tree(radius-1, extent, depth-1, right)

def backwardtree(radius, extent, depth, turtboi):
    if depth > 0:
        right = turtboi
        right.pensize(depth)
        if depth > 3:
            right.pencolor(79, 30, 26)
        elif depth > 2:
            right.pencolor('#633936')
        else:
            leaf = random.choice(['#C91E0A', '#753a36', '#DF3908', '#EDA421', '#E98604', '#A79F0F', '#8B9216'])
            right.pencolor(leaf)

        left = turtboi.clone()

        right.circle(radius, -extent)
        left.circle(-radius, -extent)

        backwardtree(radius-1, extent, depth-1, left)
        backwardtree(radius-1, extent, depth-1, right)

tree(rad, ext, depth, harry)

harry.penup()
harry.goto(0, 0)
harry.setheading(90)
harry.pendown()

backwardtree(rad, ext, depth, harry)

harry.penup()
harry.goto(0, 0)
harry.setheading(180)
harry.pendown()

input()

tree(rad, ext, depth, harry)

harry.penup()
harry.goto(0, 0)
harry.setheading(180)
harry.pendown()

backwardtree(rad, ext, depth, harry)

exitonclick()