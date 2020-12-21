import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y



class Circle:
    """Klasa reprezentująca okręgi na płaszczyźnie."""

    def __init__(self, x, y, radius):
        if radius < 0:
            raise ValueError("promień ujemny")
        self.pt = Point(x, y)
        self.radius = radius

    def __repr__(self):
        return str((Circle.__name__,self.pt.x,self.pt.y,self.radius))# "Circle(x, y, radius)"

    def __eq__(self, other):
        return (self.pt.x == other.pt.x and self.pt.y == other.pt.y and self.radius == other.radius)

    def __ne__(self, other):
        return not (self.pt.x == other.pt.x and self.pt.y == other.pt.y and self.radius==other.radius)

    def area(self):
        return ((self.radius**2)*3.14)# pole powierzchni

    def move(self, x, y):
        return Point(self.pt.x+x,self.pt.y+y)# przesuniecie o (x, y)

    def cover(self, other):
        distance =math.sqrt(((self.pt.x-other.pt.x)**2)+((self.pt.y-other.pt.y)**2))
        if (self.__eq__(other)):
            return self
        elif((distance+other.radius)<(self.radius)):
            return self
        elif ((distance + self.radius) < (other.radius)):
            return other
        elif ((self.radius+other.radius <= distance) and (self.radius>=other.radius)):
            return Circle(((self.pt.x+other.pt.x)/2),((self.pt.y+other.pt.y)/2),((distance/2)+self.radius))
        elif ((self.radius+other.radius <= distance) and (self.radius<=other.radius)):
            return Circle(((self.pt.x+other.pt.x)/2),((self.pt.y+other.pt.y)/2),((distance/2)+other.radius))
        elif ((self.radius+other.radius >= distance) and (self.radius>=other.radius)):
            return Circle(((self.pt.x+other.pt.x)/2),((self.pt.y+other.pt.y)/2),((distance/2)+self.radius))
        elif ((self.radius+other.radius >= distance) and (other.radius>=self.radius)):
            return Circle(((self.pt.x+other.pt.x)/2),((self.pt.y+other.pt.y)/2),((distance/2)+other.radius))





# Kod testujący moduł.

import unittest

class TestCircle(unittest.TestCase):

    def setUp(self):
        self.circle = Circle(1, 1, 4)
        self.circle1 = Circle(1,1,2)
        self.circle2 = Circle(1,1,4)
        self.circle3 = (1,5,2)

    def test__repr__(self):
        self.assertEqual(self.circle.__repr__(), "('Circle', 1, 1, 4)")

    def test__eq__(self):
        self.assertEqual(self.circle.__eq__(Circle(1, 1, 4)), True)
        self.assertEqual(self.circle.__eq__(Circle(2, 1, 4)), False)

    def test__ne__(self):
        self.assertEqual(self.circle.__ne__(Circle(1, 1, 4)), False)
        self.assertEqual(self.circle.__ne__(Circle(2, 1, 4)), True)


    def test_area(self):
        self.assertEqual(self.circle.area(), 50.24)

    def test_move(self):
        self.assertEqual(self.circle.move(1, 2).x, 2)
        self.assertEqual(self.circle.move(1, 2).y, 3)

    def test_cover(self):
        self.assertEqual(self.circle.cover(Circle(1,1,4)),Circle(1,1,4))
        self.assertEqual(self.circle.cover(Circle(1, 1, 2)), Circle(1, 1, 4))
        self.assertEqual(self.circle.cover(Circle(1, 1, 6)), Circle(1, 1, 6))
        self.assertEqual(self.circle.cover(Circle(1, 9, 2)), Circle(1, 5, 8))
        self.assertEqual(self.circle.cover(Circle(1, 19, 10)), Circle(1,10,19))
        self.assertEqual(self.circle.cover(Circle(1, 5, 4)), Circle(1,3,6))
        self.assertEqual(self.circle.cover(Circle(1, 5, 6)), Circle(1, 3, 8))



    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()

