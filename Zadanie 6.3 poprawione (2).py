import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y



class Triangle:
    """Klasa reprezentująca trójkąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
        self.pt3 = Point(x3, y3)

    def __str__(self):
        string_1=str((self.pt1.x,self.pt1.y,self.pt2.x,self.pt2.y,self.pt3.x,self.pt3.y))
        return string_1

    def __repr__(self):
        string_2=str((Triangle.__name__,(self.pt1.x,self.pt1.y,self.pt2.x,self.pt2.y,self.pt3.x,self.pt3.y)))
        return string_2# "Triangle(x1, y1, x2, y2, x3, y3)"

    def __eq__(self, other):
        if ((self.pt1.x==other.pt1.x and self.pt1.y==other.pt1.y ) or (self.pt1.x==other.pt2.x and self.pt1.y==other.pt2.y ) or (self.pt1.x==other.pt3.x and self.pt1.y==other.pt3.y )):
            if ((self.pt2.x == other.pt1.x and self.pt2.y == other.pt1.y) or (
                    self.pt2.x == other.pt2.x and self.pt2.y == other.pt2.y) or (self.pt2.x == other.pt3.x and self.pt2.y==other.pt3.y)):
                if ((self.pt3.x == other.pt1.x and self.pt3.y == other.pt1.y) or (
                        self.pt3.x == other.pt2.x and self.pt3.y == other.pt2.y) or (
                        self.pt3.x == other.pt3.x and self.pt3.y == other.pt3.y)):
                    return bool(1)

        else:
            return bool(0)

    def __ne__(self, other):        # obsługa tr1 != tr2
        return not self == other

    def center(self):
        a=max(self.pt1.x,self.pt2.x,self.pt3.x)  # zwraca środek trójkąta
        b = min(self.pt1.x, self.pt2.x, self.pt3.x)
        c = max(self.pt1.y, self.pt2.y, self.pt3.y)
        d = min(self.pt1.y, self.pt2.y, self.pt3.y)
        e=((a+b)/2)
        f=((c+d)/2)
        return Point(e,f)

    def area(self):
        AB=math.sqrt(((self.pt2.x-self.pt1.x)**2)+((self.pt2.y-self.pt1.y)**2))
        BC=math.sqrt(((self.pt3.x-self.pt2.x)**2)+((self.pt3.y-self.pt2.y)**2))
        CA=math.sqrt(((self.pt1.x-self.pt3.x)**2)+((self.pt1.y-self.pt3.y)**2))
        p=((AB+BC+CA)/2)
        s=round(math.sqrt(p*(p-AB)*(p-BC)*(p-CA)))
        return s# pole powierzchni

    def move(self, x, y):
        return Triangle(self.pt1.x+x,self.pt1.y+y,self.pt2.x+x,self.pt2.y+y,self.pt3.x+x,self.pt3.y+y)      # przesunięcie o (x, y)


# Kod testujący moduł.

import unittest

class TestTriangle(unittest.TestCase):

    def setUp(self):
        self.trojkat5 = Triangle(1,1,3,1,2,3)

    def test__str__(self):
        self.assertEqual(self.trojkat5.__str__(),'(1, 1, 3, 1, 2, 3)')

    def test__repr__(self):
        self.assertEqual(self.trojkat5.__repr__(),"('Triangle', (1, 1, 3, 1, 2, 3))")

    def test__eq__(self):
        self.assertEqual(self.trojkat5.__eq__(Triangle(1,1,3,1,2,3)), True)
        self.assertEqual(self.trojkat5.__eq__(Triangle(2, 1, 3, 1, 2, 3)), False)

    def test__ne__(self):
        self.assertEqual(self.trojkat5.__ne__(Triangle(1,1,3,1,2,3)), False)
        self.assertEqual(self.trojkat5.__ne__(Triangle(2, 1, 3, 1, 2, 3)), True)

    def test_center(self):
        self.assertEqual(self.trojkat5.center().x,2)
        self.assertEqual(self.trojkat5.center().y,2)

    def test_area(self):
        self.assertEqual(self.trojkat5.area(), 2)

    def test_move(self):
        self.assertEqual(self.trojkat5.move(1,2),Triangle(2,3,4,3,3,5))


    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()
