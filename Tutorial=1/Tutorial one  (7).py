x = float(input("Enter x-coordinate: "))
y = float(input("Enter y-coordinate: "))

if x > 0 and y > 0:
    print("Point is in Quadrant 1")
elif x < 0 and y > 0:
    print("Point is in Quadrant 2")
elif x < 0 and y < 0:
    print("Point is in Quadrant 3")
elif x > 0 and y < 0:
    print("Point is in Quadrant 4")
elif x == 0 and y == 0:
    print("Point is at the origin")
elif x == 0:
    print("Point is on the Y-axis")
else:
    print("Point is on the X-axis")
