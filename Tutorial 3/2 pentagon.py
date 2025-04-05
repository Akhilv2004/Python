import turtle

pentagon = turtle.Turtle()
pentagon.speed(5)

for i in range(5):
    pentagon.forward(100)
    pentagon.right(72)

pentagon.hideturtle()
turtle.done()
