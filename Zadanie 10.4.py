class Queue:

    def __init__(self, size=5):
        self.n = size + 1         # faktyczny rozmiar tablicy
        self.items = self.n * [None]
        self.head = 0           # pierwszy do pobrania
        self.tail = 0           # pierwsze wolne

    def is_empty(self):
        return self.head == self.tail

    def is_full(self):
        return (self.head + self.n-1) % self.n == self.tail

    def put(self, data):
        if ((self.head + self.n-1) % self.n == self.tail):
            raise Exception
        self.items[self.tail] = data
        self.tail = (self.tail + 1) % self.n

    def get(self):
        if (self.head==self.tail):
            raise Exception
        data = self.items[self.head]
        self.items[self.head] = None      # usuwam referencję
        self.head = (self.head + 1) % self.n
        return data


import unittest

class TestQueue(unittest.TestCase):

    def setUp(self):
        self.a=Queue()
        self.a.put(1)

        self.b = Queue()

        self.c = Queue()
        self.c.put(1)
        self.c.put(1)
        self.c.put(1)
        self.c.put(1)
        self.c.put(1)

    def test_is_full(self):
        self.assertEqual(self.b.is_full(),False)
        self.assertEqual(self.c.is_full(),True)


    def test_is_empty(self):
        self.assertEqual(self.b.is_empty(),True)
        self.assertEqual(self.a.is_empty(), False)

    def test_get(self):
        self.assertEqual(self.a.get(),1)

    def test_get_bad(self):
        with self.assertRaises(Exception):
            self.b.get()

    def test_put_bad(self):
        with self.assertRaises(Exception):
            self.c.put(1)


    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()