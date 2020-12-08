import math
import unittest

def heron(a, b, c):
    if ((a+b) < c or (a+c) < b or (c+b) < a):
        raise ValueError
    else:
        p = ((a + b + c) / 2)
        s = round(math.sqrt(p * (p - a) * (p - b) * (p - c)))
        return s


class Test(unittest.TestCase):

    def test_heron(self):
        self.assertEqual(heron(3, 4, 5), 6)

    def test_heron_bad(self):
        with self.assertRaises(ValueError):
            heron(1, 1, 10)

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()
