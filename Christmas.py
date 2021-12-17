# Copyright Zhoukunyang
# This is a python script for christmas 
# if you think this script will be helpful to you, just use it

from math import e
import turtle as t
import random as r
import time

from turtle import *
from random import *

def drawlight():
    if r.randint(0,30) == 0:
        color('tomato')
        circle(6)
    
    elif r.randint(0,30) == 1:
        color('orange')
        circle(3)
    
    else:
        color('green')

def tree(d,s):
    if d<=0: return
    forward(s)
    tree(d -1,s * .8)
    right(120)
    drawlight()
    tree(d -3,s * .5)
    right(120)
    tree(d -3,s * .5)
    right(120)    
    backward(s)

def drawsnow():
    t.ht()
    t.pensize(2)
    for i in range(180):
        t.pencolor("white")
        t.pu()
        t.setx(r.randint(-350,350))
        t.sety(r.randint(-100,350))
        t.pd()
        dens = 6
        snowsize = r.randint(1,10)
        for j in range(dens):
            t.fd(int(snowsize))
            t.backward(int(snowsize))
            t.right(int(360/dens))

def star():
    time.sleep(0.000005)
    speed(0)
    hideturtle()
    for i in range(18):
        pensize(randint(3,5))
        x = (randint(-350,350))
        y = (randint(0,350))
        pencolor('gold')
        penup()
        goto(x,y)
        for i in range(5):
            forward(20)
            right(144)

if __name__ == '__main__':
    n  = 100
    t.pensize(2)
    speed('fastest')
    screensize(bg='black')
    left(90)
    forward(3*n)
    color('orange','yellow')
    begin_fill()
    left(126)
    for i in range(5):
        forward(n / 5)
        right(144)
        forward(n/5)
        left(72)
    end_fill()
    right(126)

    color("green")
    backward(n*4.8)

    tree(15,n)
    backward(n/2)
    for i in range(200):
        a = 200-400*r.random()
        b = 10-20*r.random()
        up()
        forward(b)
        left(90)
        forward(a)
        down()

        if r.randint(0,1) == 0:
            color('tomato')
        else:
            color('wheat')
        
        circle(2)
        up()
        backward(a)
        right(90)
        backward(b)
    
    t.color('dark red','red')
    # You can change below word. For example,"Merry christmas {Your girl/boy friend name}"
    t.write("Merry christmas Cao Z X",align='center',font=("Comic Sans Ms",40,"bold"))

    drawsnow()
    window_w = t.window_width()
    window_h = t.window_height()

    t.fillcolor("yellow")
    t.penup()
    t.goto(-100,350)
    t.pendown()
    t.begin_fill()
    t.left(30)
    t.circle(100,180)
    t.left(120)
    t.circle(-200,60)
    t.end_fill()

    star()
    t.done()
