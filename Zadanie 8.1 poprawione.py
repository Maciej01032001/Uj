

#a * x + b * y + c = 0

def solve1(a,b,c):
    if ((a==0 and b==0) or (a==0 and c==0) or (b==0 and c==0)):
        raise ValueError
    elif (a!=0 and b!=0 and c!=0):
        a1=a/-b
        c1=c/-b
        wynik="y = {}x + {}".format(a1,c1)
        return wynik
    elif (a==0):
        c1 = c /-b
        wynik= "y = {}".format(c1)
        return wynik
    elif (b==0):
        c1 = c /-a
        wynik = "x = {}".format(c1)
        return wynik
    elif (c==0):
        a1= a/-b
        wynik = "y = {}x".format(a1)
        return wynik


import unittest

class Test(unittest.TestCase):

    def test_solve1(self):
        self.assertEqual(solve1(5,-1,8),"y = 5.0x + 8.0")
        self.assertEqual(solve1(0, -1, 8), "y = 8.0")
        self.assertEqual(solve1(1, 0, 8), "x = -8.0")
        self.assertEqual(solve1(5, -1, 0), "y = 5.0x")

    def test_solve1_bad(self):
        with self.assertRaises(ValueError):
            solve1(0, 0, 10)

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()

