import turtle
import colorsys
t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor("black")
t.speed(0)
n=200
h=0
for i in range(150):
    c=colorsys.hls_to_rgb(h,1,0.8)
    h+=1/n
    t.color(c)
    t.left(8)
    t.forward(100)
    t.right(175)
    for j in range(4):
        t.forward(1*1)
        t.left(6)


turtle.done()