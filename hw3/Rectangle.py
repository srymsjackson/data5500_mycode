class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    

# Instantiate the object
rect = Rectangle(5, 3)

# Prints the area
print(rect.area())

