class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y



class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        # W poleceniu jest wspomniany lewy dolny róg i prawy górny, zakładm że w tej kolejnosci są podane
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):
            string=str((self.pt1.x,self.pt1.y,self.pt2.x,self.pt2.y))
            return string# "[(x1, y1), (x2, y2)]"

    def __repr__(self):
        string=str((Rectangle.__name__, (self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y)))# "Rectangle(x1, y1, x2, y2)"
        return string

    def __eq__(self, other):   # obsługa rect1 == rect2
        if (self.pt1.x == other.pt1.x and self.pt2.x == other.pt2.x and self.pt1.y == other.pt1.y and self.pt2.y == other.pt2.y):
            return bool(1)
        else:
            return bool(0)

    def __ne__(self, other):        # obsługa rect1 != rect2
        return not self == other

    def center(self):
        return Point(((self.pt2.x-self.pt1.x)/2),((self.pt2.y-self.pt1.y)/2))# zwraca środek prostokąta

    def area(self):
        return ((self.pt2.x-self.pt1.x)*(self.pt2.y-self.pt1.y))# pole powierzchni

    def move(self, x, y):     # przesunięcie o (x, y)
        return Rectangle((self.pt1.x)+x,(self.pt1.y)+y,(self.pt2.x)+x,(self.pt2.y)+y)
# Kod testujący moduł.


import unittest

class TestRectangle(unittest.TestCase):

    def setUp(self):
        self.prostokat = Rectangle(0, 0, 4, 4)

    def test__str__(self):
        self.assertEqual(self.prostokat.__str__(), '(0, 0, 4, 4)')

    def test__repr__(self):
        self.assertEqual(self.prostokat.__repr__(), "('Rectangle', (0, 0, 4, 4))")

    def test__eq__(self):
        self.assertEqual(self.prostokat.__eq__(Rectangle(0,0,4,4)), True)
        self.assertEqual(self.prostokat.__eq__(Rectangle(1, 0, 4, 4)), False)

    def test__ne__(self):
        self.assertEqual(self.prostokat.__ne__(Rectangle(0,0,4,4)), False)
        self.assertEqual(self.prostokat.__ne__(Rectangle(1,0,4,4)), True)

    def test_center(self):
        self.assertEqual(self.prostokat.center().x, (2.0))
        self.assertEqual(self.prostokat.center().y, (2.0))

    def test_area(self):
        self.assertEqual(self.prostokat.area(), 16)

    def test_move(self):
        self.assertEqual(self.prostokat.move(1, 2), Rectangle(1,2,5,6))

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()
