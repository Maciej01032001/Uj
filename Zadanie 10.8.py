import random

class RandomQueue:

    def __init__(self, size=5):
        self.n = size
        self.items = self.n * [None]
        self.i=0

    def insert(self, data):
        if (self.i==self.n):
            raise ValueError
        self.items[self.i]=data
        self.i=self.i+1

    def remove(self):
        if (self.i==0):
            raise ValueError
        a=random.randrange(0,(self.i))  # zwraca losowy element
        b=(self.items[a])
        while(a!=(self.n-1)):
            self.items[a]=self.items[a+1] # przesuwa reszte elementów
            a=a+1
        self.items[self.i-1]=None
        self.i=self.i-1
        return b

    def is_empty(self):
        if (self.i==0):
            return True
        else:
            return False

    def is_full(self):
        if (self.i==self.n):
            return True
        else:
            return False

    def clear(self):
        self.items = self.n * [None]
        self.i=0    # czyszczenie listy

a=RandomQueue() #Test pomocniczy ktory stworzyłem podczas pisania,
a.insert(1)     #sprawdzajacy czy program dobrze przesuwa elementy i nie gubi żadnego
a.insert(2)
a.insert(3)
print(a.remove())
print(a.remove())
print(a.remove())
print(a.is_empty())






import unittest

class TestQueue(unittest.TestCase):

    def setUp(self):
        self.a=RandomQueue()
        self.a.insert(1)

        self.b = RandomQueue()

        self.c = RandomQueue()
        self.c.insert(1)
        self.c.insert(1)
        self.c.insert(1)
        self.c.insert(1)
        self.c.insert(1)

        self.d = RandomQueue()
        self.d.insert(1)
        self.d.insert(1)
        self.d.insert(1)
        self.d.insert(1)
        self.d.insert(1)
        self.d.clear()

    def test_remove(self):
        self.assertEqual(self.a.remove(),1)
        self.assertEqual(self.c.remove(),1)


    def test_is_empty(self):
       self.assertEqual(self.b.is_empty(),True)
       self.assertEqual(self.a.is_empty(),False)

    def test_is_full(self):
       self.assertEqual(self.c.is_full(),True)
       self.assertEqual(self.b.is_full(),False)

    def test_clear(self):
        self.assertEqual(self.d.is_empty(),True)

    def test_clear_2(self):
        with self.assertRaises(ValueError):
            self.d.remove()

    def test_remove_bad(self):
        with self.assertRaises(ValueError):
            self.b.remove()

    def test_insert_bad(self):
        with self.assertRaises(ValueError):
            self.c.insert(1)


    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()