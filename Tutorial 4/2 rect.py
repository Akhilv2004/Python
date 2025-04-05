class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

rect = Rectangle(10, 5)
print("Area of the rectangle:", rect.area())
