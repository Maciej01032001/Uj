

#a * x + b * y + c = 0

def solve1(a,b,c):
    if (a==0 or b==0):
        raise ValueError
    a1=a/-b
    c1=c/-b
    wynik=c1/-a
    return wynik


import unittest

class Test(unittest.TestCase):

    def test_solve1(self):
        self.assertEqual(solve1(5,-1,8),-1.6)
        self.assertEqual(solve1(5, -1, 5), -1)
        self.assertEqual(solve1(5, -1, -5), 1)

    def test_solve1_bad(self):
        with self.assertRaises(ValueError):
            solve1(0, 0, 10)

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()

