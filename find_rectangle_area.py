''' Define a class named Rectangle which can be constructed by a length and width. 
The Rectangle class has a method which can compute the area and Perimeter.'''

class Rectangle:
    def __init__(self, l, w):
        self.length = l
        self.width = w
    def rectangle_area(self):
        return self.length*self.width
newRectangle = Rectangle(12, 10)
print(newRectangle.rectangle_area())