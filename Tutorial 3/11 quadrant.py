def find_quadrant(x, y):
    if x > 0 and y > 0:
        return "Quadrant 1"
    elif x < 0 and y > 0:
        return "Quadrant 2"
    elif x < 0 and y < 0:
        return "Quadrant 3"
    elif x > 0 and y < 0:
        return "Quadrant 4"
    elif x == 0 and y == 0:
        return "Origin"
    elif x == 0:
        return "On the Y-axis"
    elif y == 0:
        return "On the X-axis"

x = float(input("Enter x-coordinate: "))
y = float(input("Enter y-coordinate: "))
print(find_quadrant(x, y))
