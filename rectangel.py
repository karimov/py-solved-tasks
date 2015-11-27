class Rectangle:
    """ A class to manufacture rectangle objects """
    def __init__(self, posn, w, h):
        """ Initialize rectangle at posn, with width w, height h """
        self.corner = posn
        self.width = w
        self.height = h
    def __str__(self):
        return  "({0}, {1}, {2})".format(self.corner, self.width, self.height)
    def area(self):
        return self.width * self.height
    def perimeter(self):
    	return 2*(self.width + self.height)
    def flip(self):
    	(self.width, self.height) = (self.height, self.width)
    def contains(self, point):
    	if self.corner.x < point.x <= self.width and self.corner.y < point.y <= self.height:
    	   return True
    	return False
    def ovelap(self, rectangle):
    	if self.corner.x <= rectangle.corner.x <= self.width and self.corner.y <= rectangle.corner.y <= self.height:
    	   return True
    	return False   
        
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return  "(x={0}, y={1})".format(self.x, self.y)
    def __add__(self, point):
    	return (self.x + point.x, self.y + point.y)
    def __sub__(self, point):
    	return (self.x - point.x, self.y-point.y)
    def __rmul__(self, other):
    	return Point(other * self.x,  other * self.y)
    def __mul__(self, other):
    	return self.x * other.x + self.y * other.y
    	
    	
    	
def between(t1, t2):
