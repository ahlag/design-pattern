## Whenever you  have an interface taking some sort of 
## base classes, you should be able t o stick in any of
## its inheritors. So, if you take a rectangle, you should
## be able to stick in a square in ther and everything should
## work fine.
class Rectangle:
    
    def __init__(self, width, height):
        self._width = width
        self._height = height
        
    @property
    def area(self):
        return self._height * self._width
    
    def __str__(self):
        return f'Width: {self.width} Height: {self.height}'
        
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        self._width = value
        
    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

class Square(Rectangle):
    
    def __init__(self, size):
        Rectangle.__init__(self, size, size)
    
    ## Violation
    @Rectangle.width.setter
    def width(self, value):
        self._width = self._height = value
    
    ## Violation
    @Rectangle.height.setter
    def height(self, value):
        self._width = self._height = value
    
## Only works for the rectangle but not any of its derived classes
def use_it(rc):
    w = rc.width
    
    ## Violation
    rc.height = 10
    expected = int(w*10)
    print(f'Expected an area of {expected}, got {rc.area}')
    
rc = Rectangle(2,3)
print(rc.height)
use_it(rc)

sq = Square(5)
use_it(sq)