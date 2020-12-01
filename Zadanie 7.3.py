class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        # W poleceniu jest wspomniany lewy dolny róg i prawy górny, zakładm że w tej kolejnosci są podane
        self.pt1 = [x1, y1]
        self.pt2 = [x2, y2]

    def __str__(self):
            return (self.pt1[0],self.pt1[1],self.pt2[0],self.pt2[1])# "[(x1, y1), (x2, y2)]"

    def __repr__(self):        # "Rectangle(x1, y1, x2, y2)"
        return Rectangle.__name__, (self.pt1[0], self.pt1[1], self.pt2[0], self.pt2[1])

    def __eq__(self, other):   # obsługa rect1 == rect2
        if (self.pt1 == other.pt1 and self.pt2 == other.pt2):
            return bool(1)
        else:
            return bool(0)

    def __ne__(self, other):        # obsługa rect1 != rect2
        return not self == other

    def center(self):
        return (((self.pt2[0]-self.pt1[0])/2),((self.pt2[1]-self.pt1[1])/2))# zwraca środek prostokąta

    def area(self):
        return ((self.pt2[0]-self.pt1[0])*(self.pt2[1]-self.pt1[1]))# pole powierzchni

    def move(self, x, y):     # przesunięcie o (x, y)
        return [self.pt1[0]+x,self.pt1[1]+y,self.pt2[0]+x,self.pt2[1]+y]

    def intersection(self, other):
        if (self.pt1==other.pt1 and self.pt2==other.pt2):
            try:
                raise ValueError
            except ValueError:
                return ("Jest to ten sam prostokat")
        if (self.pt2[0]<other.pt1[0] or self.pt2[1]<other.pt1[1] or other.pt2[0]<self.pt1[0] or other.pt2[1]< self.pt1[1]):
            try:
                raise ValueError
            except ValueError:
                return ("Prostokaty nie maja czesci wspolnej")
        else:
            return ("Prostokaty maja czesc wspolna")

    def cover(self, other):
        max_x = max(self.pt1[0],self.pt2[0],other.pt1[0],other.pt2[0])
        min_x = min(self.pt1[0],self.pt2[0],other.pt1[0],other.pt2[0])
        max_y = max(self.pt1[1],self.pt2[1],other.pt1[1],other.pt2[1])
        min_y = min(self.pt1[1],self.pt2[1],other.pt1[1],other.pt2[1])
        return (min_x,min_y,max_x,max_y)
        # prostąkąt nakrywający oba

    def make4(self):
        return ((self.pt1[0],self.pt1[1],((self.pt2[0]-self.pt1[0])/2),((self.pt2[1]-self.pt1[1])/2)),
                (((self.pt2[0] - self.pt1[0]) / 2),((self.pt2[1]-self.pt1[1])/2)-(self.pt2[1]/2),self.pt2[0],(self.pt2[1]/2)),
                (self.pt1[0],(self.pt2[1]-self.pt1[1])/2,(self.pt2[0]-self.pt1[0])/2,self.pt2[1]),
                ((self.pt2[0]-self.pt1[0])/2,(self.pt2[1]-self.pt1[1])/2,self.pt2[0],self.pt2[1]))


# Kod testujący moduł.

import unittest

class TestRectangle(unittest.TestCase):

    def setUp(self):
        self.prostokat = Rectangle(0, 0, 4, 4)
        self.prostokat1 = Rectangle(5, 5, 9, 9)
        self.prostokat2 = Rectangle(0,0,4,4)
        self.prostokat3= Rectangle(0,0,10,10)

    def test__str__(self):
        self.assertEqual(self.prostokat.__str__(), (0, 0, 4, 4))

    def test__repr__(self):
        self.assertEqual(self.prostokat.__repr__(), ('Rectangle', (0, 0, 4, 4)))

    def test__eq__(self):
        self.assertEqual(self.prostokat.__eq__(Rectangle(0,0,4,4)), True)
        self.assertEqual(self.prostokat.__eq__(Rectangle(1, 0, 4, 4)), False)

    def test__ne__(self):
        self.assertEqual(self.prostokat.__ne__(Rectangle(0,0,4,4)), False)
        self.assertEqual(self.prostokat.__ne__(Rectangle(1,0,4,4)), True)

    def test_center(self):
        self.assertEqual(self.prostokat.center(), (2.0, 2.0))

    def test_area(self):
        self.assertEqual(self.prostokat.area(), 16)

    def test_move(self):
        self.assertEqual(self.prostokat.move(1, 2), [1,2,5,6])

    def test_intersection(self):
        self.assertEqual(self.prostokat.intersection(self.prostokat1),"Prostokaty nie maja czesci wspolnej")
        self.assertEqual(self.prostokat.intersection(self.prostokat2), "Jest to ten sam prostokat")
        self.assertEqual(self.prostokat.intersection(self.prostokat3), "Prostokaty maja czesc wspolna")

    def test_cover(self):
        self.assertEqual(self.prostokat.cover(self.prostokat1),(0,0,9,9))

    def test_make4(self):
        self.assertEqual(self.prostokat.make4(),((0,0,2,2),(2,0,4,2),(0,2,2,4),(2,2,4,4)))

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()
