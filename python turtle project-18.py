import turtle
turtle.bgcolor("black")
turtle.speed(0)
turtle.pensize(2)
turtle.pencolor("blue")
turtle.penup()
turtle.backward(250)
turtle.left(90)
turtle.forward(200)
turtle.pendown()
def drawcircle(radius):
    for i in range(2):
        turtle.circle(radius)
        radius=radius-4

def drawdesign():
    for i in range(10):
        drawcircle(30)
        turtle.right(36)

drawdesign()
turtle.penup()
turtle.right(90)
turtle.forward(180)
turtle.pendown()
turtle.pencolor("red")
drawdesign()

turtle.penup()
turtle.right(90)
turtle.forward(180)
turtle.pendown()
turtle.pencolor("green")
drawdesign()

turtle.penup()
turtle.right(90)
turtle.forward(180)
turtle.pendown()
turtle.pencolor("yellow")
drawdesign()

turtle.penup()
turtle.left(90)
turtle.forward(180)
turtle.pendown()
turtle.pencolor("pink")
drawdesign()

turtle.penup()
turtle.right(90)
turtle.backward(200)
turtle.pendown()
turtle.pencolor("gray")
drawdesign()

turtle.penup()
turtle.right(150)
turtle.forward(150)
turtle.pendown()
turtle.pencolor("lime")
drawdesign()

turtle.penup()
turtle.right(90)
turtle.backward(100)
turtle.pendown()
turtle.pencolor("navy")
drawdesign()

turtle.penup()
turtle.right(90)
turtle.backward(200)
turtle.pendown()
turtle.pencolor("orange")
drawdesign()

turtle.penup()
turtle.left(80)
turtle.backward(100)
turtle.pendown()
turtle.pencolor("purple")
drawdesign()

turtle.penup()
turtle.left(90)
turtle.backward(200)
turtle.pendown()
turtle.pencolor("silver")
drawdesign()


turtle.done()