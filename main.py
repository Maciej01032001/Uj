import math

class Circle:
    """Klasa reprezentująca okręgi na płaszczyźnie."""

    def __init__(self, x, y, radius):
        if radius < 0:
            raise ValueError("promień ujemny")
        self.pt = [x, y]
        self.radius = radius

    def __repr__(self):
        return Circle.__name__,(self.pt[0],self.pt[1],self.radius)# "Circle(x, y, radius)"

    def __eq__(self, other):
        return self.pt == other.pt and self.radius == other.radius

    def __ne__(self, other):
        return not self == other

    def area(self):
        return ((self.radius**2)*3.14)# pole powierzchni

    def move(self, x, y):
        return (self.pt[0]+x,self.pt[1]+y)# przesuniecie o (x, y)

    def cover(self, other):
        odleglosc = math.sqrt(((self.pt[0]-other.pt[0])**2)+((self.pt[1]-other.pt[1])**2))
        srodek = (((self.pt[0]+other.pt[0])/2),((self.pt[1]+other.pt[1])/2))
        if (self.radius==other.radius and self.pt==other.pt):
            try:
                raise ValueError
            except ValueError:
               return ("To ten sam okreg")
        elif (self.radius+other.radius<=odleglosc):
            return (srodek,((odleglosc+self.radius+other.radius)/2))
        elif ((odleglosc+other.radius)<self.radius):
            return (self.pt[0],self.pt[1],self.radius)
        elif ((odleglosc+self.radius)<other.radius):
            return (other.pt[0],other.pt[1],other.radius)
        elif (odleglosc<self.radius):
            return (self.pt,odleglosc+other.radius)
        elif (odleglosc<other.radius):
            return (other.pt,odleglosc+self.radius)




# Kod testujący moduł.

import unittest

class TestCircle(unittest.TestCase):

    def setUp(self):
        self.circle = Circle(1, 1, 4)
        self.circle1 = Circle(1,1,2)

    def test__repr__(self):
        self.assertEqual(self.circle.__repr__(), ('Circle', (1, 1, 4)))

    def test__eq__(self):
        self.assertEqual(self.circle.__eq__(Circle(1, 1, 4)), True)
        self.assertEqual(self.circle.__eq__(Circle(2, 1, 4)), False)

    def test__ne__(self):
        self.assertEqual(self.circle.__ne__(Circle(1, 1, 4)), False)
        self.assertEqual(self.circle.__ne__(Circle(2, 1, 4)), True)


    def test_area(self):
        self.assertEqual(self.circle.area(), 50.24)

    def test_move(self):
        self.assertEqual(self.circle.move(1, 2), (2, 3))

    def test_cover(self):
        self.assertEqual(self.circle.cover(Circle(9,1,4)),((5,1),8))
        self.assertEqual(self.circle.cover(self.circle1),(1,1,4))
        self.assertEqual(self.circle.cover(self.circle), "To ten sam okreg")

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()

