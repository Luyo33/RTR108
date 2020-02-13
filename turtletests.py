from turtle import *

#draw fractal spike
def fspike(s, n, t):
    if(n < 1):
        t.fd(s/3)
        t.lt(60)
        t.fd(s/3)
        t.rt(120)
        t.fd(s/3)
        t.lt(60)
        t.fd(s/3)
    else:
        t.fd(s/3)
        t.lt(60)
        fspike(s/3, n-1, t)
        t.rt(120)
        fspike(s/3, n-1, t)
        t.lt(60)
        t.fd(s/3)
#draw a fractal star
def fstar(s, n, t):
    t.penup()
    t.lt(120)
    t.fd(s)
    t.pendown()
    t.rt(120)
    t.hideturtle()
    for i in range(6):
        fspike(s, n, t)
        t.rt(60)
        

t = Turtle()

fstar(300, 4, t)
