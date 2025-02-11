import turtle
import math

"""PUT YOUR FUNCTIONS HERE"""
def polyline(t:turtle.Turtle,n, length, angle):
    for i in range(n):
        t.forward(length)
        t.left(angle)

def arc(t:turtle.Turtle,radius, angle):
    arc_length = 2 * math.pi * radius * angle / 360
    n = 30
    length = arc_length / n
    step_angle = angle / n
    polyline(t,n, length, step_angle)

def jump(t: turtle.Turtle, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def rectangle(t:turtle.Turtle, length, height):
    for i in (length, height, length, height):
        t.forward(i)
        t.left(90)

def square(t:turtle.Turtle,length):
    rectangle(t,length,length)

def draw_ribbon(t,x,y,length,height,color="green"):
    jump(t,x,y)
    t.fillcolor(color)
    t.begin_fill()
    rectangle(t,length,height)
    t.end_fill()

def draw_bow(t,x,y,bow_size):
    jump(t,x,y)
    t.right(15)
    print(t.pos())
    arc(t,bow_size,120)
    t.left(60)
    print(t.pos())
    arc(t,bow_size,120)
    pass

def draw_present(t:turtle.Turtle,x,y,length,height,ribbon_width,color="red"):
    jump(t,x,y)
    t.fillcolor(color)
    t.begin_fill()
    rectangle(t,length,height)
    t.end_fill()
    p_center=x+(length/2)
    r_x= p_center-(ribbon_width/2)
    draw_ribbon(t,r_x,y,ribbon_width,height)
    r_y = (y + (height / 2)) - (ribbon_width / 2)
    draw_ribbon(t,x,r_y,length,ribbon_width)
    draw_bow(t,p_center,y+height,length/3)



# Create a turtle object
t = turtle.Turtle()

# Hide the turtle and set speed
t.speed(10)  # 1 is slow, 10 is fast, 0 is instant
t.hideturtle()

# Create a window to draw in
# Create a new turtle screen and set its background color
screen = turtle.Screen()
screen.bgcolor("darkblue")
# Set the width and height of the screen
screen.setup(width=600, height=600)
# Clear the screen
t.clear()

"""PUT YOUR DRAW CALLS TO FUNCTIONS HERE"""

t.color("yellow")

draw_present(t,-10,-50,69,69,5)

# Close the turtle graphics window when clicked
turtle.exitonclick()