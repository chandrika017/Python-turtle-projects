import turtle
turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(0)
for i in range(6):
    for colours in ("red","blue","green","yellow","cyan","purple"):
        turtle.color(colours)
        turtle.circle(100,100,1)
        turtle.left(10)
turtle.hideturtle()