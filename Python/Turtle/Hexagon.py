import turtle
wn=turtle.Screen()
wn.bgcolor("Yellow")
wn.title("Hexagon")
t=turtle.Turtle()
t.color("Red")
t.shape("square")
t.speed(5)
sides=6
angle=360.0/sides
for i in range(sides):
    t.forward(150)
    t.right(angle)
    
