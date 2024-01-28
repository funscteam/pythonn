from turtle import *
import colorsys

bgcolor ("black")
pensize (2)
tracer (10)
h=0

for i in range (300):
    c=colorsys.hsv_to_rgb(h,1,1)
    pencolor(c)
    h+=0.005
    right(120)
    circle(-i*0.5,120)
    circle(i*0.5,120)
    circle(i*0.5,80)

done()

