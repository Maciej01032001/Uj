

class Stack:

    def __init__(self, size=10):
        self.items = size * [None]      # utworzenie tablicy
        self.n = 0                      # liczba elementów na stosie
        self.size = size

    def is_empty(self):
        return self.n == 0

    def is_full(self):
        return self.size == self.n

    def push(self, data):
        if (self.size==self.n):
            raise ValueError
        self.items[self.n] = data
        self.n += 1

    def pop(self):
        if (self.n==0):
            raise ValueError
        self.n -= 1
        data = self.items[self.n]
        self.items[self.n] = None    # usuwam referencję
        return data


import unittest

class TestStack(unittest.TestCase):

    def setUp(self):
        self.a=Stack()
        self.a.push(1)

        self.b = Stack()

        self.c = Stack()
        self.c.push(1)
        self.c.push(1)
        self.c.push(1)
        self.c.push(1)
        self.c.push(1)
        self.c.push(1)
        self.c.push(1)
        self.c.push(1)
        self.c.push(1)
        self.c.push(1)

    def test_is_full(self):
        self.assertEqual(self.b.is_full(),False)
        self.assertEqual(self.c.is_full(),True)


    def test_is_empty(self):
        self.assertEqual(self.b.is_empty(),True)
        self.assertEqual(self.a.is_empty(), False)

    def test_pop(self):
        self.assertEqual(self.a.pop(),1)

    def test_pop_bad(self):
        with self.assertRaises(ValueError):
            self.b.pop()

    def test_push_bad(self):
        with self.assertRaises(ValueError):
            self.c.push(1)


    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()