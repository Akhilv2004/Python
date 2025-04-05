import turtle

hexagon = turtle.Turtle()
hexagon.speed(5)

for _ in range(10):
    for _ in range(6):
        hexagon.forward(60)
        hexagon.right(60)
    hexagon.right(36)

turtle.done()
