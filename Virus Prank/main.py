import turtle

a=turtle.Turtle()
a.color('green1')
a.speed()
a.hideturtle()

s=turtle.Screen()
s.bgcolor('black')
for x in range(200):
    a.forward(x)
    a.left(x-1)
turtle.done()