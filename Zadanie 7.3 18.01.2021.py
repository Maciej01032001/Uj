
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
        if ((x1>x2) or (y1>y2)):
             raise ValueError
        else:
            return None

    def __str__(self):
        string=str([(self.pt1.x,self.pt1.y),(self.pt2.x,self.pt2.y)])
        return string# "[(x1, y1), (x2, y2)]"

    def __repr__(self):
        krotka=str((self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y))# "Rectangle(x1, y1, x2, y2)"
        string="Rectangle"+krotka
        return string

    def __eq__(self, other):   # obsługa rect1 == rect2
        if (self.pt1.x == other.pt1.x and self.pt1.x == other.pt1.x and self.pt2.x == other.pt2.x and self.pt2.x == other.pt2.x):
            return bool(1)
        else:
            return bool(0)

    def __ne__(self, other):        # obsługa rect1 != rect2
        return not self == other

    def center(self):
        return Point(((self.pt2.x+self.pt1.x)/2),((self.pt2.y+self.pt1.y)/2))# zwraca środek prostokąta

    def area(self):
        return ((self.pt2.x-self.pt1.x)*(self.pt2.y-self.pt1.y))# pole powierzchni

    def move(self, x, y):     # przesunięcie o (x, y)
        return Rectangle(self.pt1.x+x,self.pt1.y+y,self.pt2.x+x,self.pt2.y+y)

    def intersection(self, other):
        max_x = min(self.pt2.x,other.pt2.x)
        min_x = max(self.pt1.x,other.pt1.x)
        max_y = min(self.pt2.y,other.pt2.y)
        min_y = max(self.pt1.y,other.pt1.y)
        return Rectangle(min_x,min_y,max_x,max_y)

    def cover(self, other):
        max_x = max(self.pt1.x,self.pt2.x,other.pt1.x,other.pt2.x)
        min_x = min(self.pt1.x,self.pt2.x,other.pt1.x,other.pt2.x)
        max_y = max(self.pt1.y,self.pt2.y,other.pt1.y,other.pt2.y)
        min_y = min(self.pt1.y,self.pt2.y,other.pt1.y,other.pt2.y)
        return Rectangle(min_x,min_y,max_x,max_y)
        # prostąkąt nakrywający oba

    def make4(self):
        return (Rectangle(self.pt1.x,self.pt1.y,((self.pt2.x+self.pt1.x)/2),((self.pt2.y+self.pt1.y)/2)),
                Rectangle(((self.pt2.x + self.pt1.x) / 2),self.pt1.y,self.pt2.x,(self.pt2.y/2)),
                Rectangle(self.pt1.x,(self.pt2.y+self.pt1.y)/2,(self.pt2.x+self.pt1.x)/2,self.pt2.y),
                Rectangle((self.pt2.x+self.pt1.x)/2,(self.pt2.y+self.pt1.y)/2,self.pt2.x,self.pt2.y))



# Kod testujący moduł.
prostokat = Rectangle(0, 0, 4, 4)


import unittest

class TestRectangle(unittest.TestCase):

    def setUp(self):
        self.prostokat = Rectangle(0, 0, 4, 4)
        self.prostokat1 = Rectangle(5, 5, 9, 9)
        self.prostokat2 = Rectangle(0,0,4,4)
        self.prostokat3= Rectangle(0,0,10,10)
        self.prostokat4 = Rectangle(0, 0, 0, 0)

    def test__str__(self):
        self.assertEqual(self.prostokat.__str__(), "[(0, 0), (4, 4)]")

    def test__repr__(self):
        self.assertEqual(self.prostokat.__repr__(),  "Rectangle(0, 0, 4, 4)")

    def test__eq__(self):
        self.assertEqual(self.prostokat.__eq__(Rectangle(0,0,4,4)), True)
        self.assertEqual(self.prostokat.__eq__(Rectangle(1, 0, 4, 4)), False)

    def test__ne__(self):
        self.assertEqual(self.prostokat.__ne__(Rectangle(0,0,4,4)), False)
        self.assertEqual(self.prostokat.__ne__(Rectangle(1,0,4,4)), True)

    def test_center(self):
        self.assertEqual(self.prostokat.center().x, 2.0)
        self.assertEqual(self.prostokat.center().y, 2.0)

    def test_area(self):
        self.assertEqual(self.prostokat.area(), 16)

    def test_move(self):
        self.assertEqual(self.prostokat.move(1, 2).pt1.x, 1)
        self.assertEqual(self.prostokat.move(1, 2).pt1.y, 2)
        self.assertEqual(self.prostokat.move(1, 2).pt2.x, 5)
        self.assertEqual(self.prostokat.move(1, 2).pt2.y, 6)

    def test_intersection(self):
        self.assertEqual(self.prostokat.intersection(Rectangle(2,2,6,6)),Rectangle(2,2,4,4))
        self.assertEqual(self.prostokat.intersection(Rectangle(3, 3, 4, 4)), Rectangle(3, 3, 4, 4))
        self.assertEqual(self.prostokat.intersection(Rectangle(3, 3, 4, 4)), Rectangle(3, 3, 4, 4))
        self.assertEqual(self.prostokat1.intersection(Rectangle(3, 3, 6, 6)), Rectangle(5, 5, 6, 6))

    def test_cover(self):
        self.assertEqual(self.prostokat.cover(self.prostokat1).pt1.x,0)
        self.assertEqual(self.prostokat.cover(self.prostokat1).pt1.y, 0)
        self.assertEqual(self.prostokat.cover(self.prostokat1).pt2.x, 9)
        self.assertEqual(self.prostokat.cover(self.prostokat1).pt2.y, 9)

    def test_make4(self):
        self.assertEqual(self.prostokat.make4(),(Rectangle(0,0,2,2),Rectangle(2,0,4,2),Rectangle(0,2,2,4),Rectangle(2,2,4,4)))

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()
