import unittest

def dynamiczny(i, j):
    if (i<0 or j<0):
        raise ValueError

    slownik = {(0, 0): 0.5}

    for y_0 in range(i+1):
        slownik[(y_0,0)]=0.0
    for x_0 in range(j+1):
        slownik[(0,x_0)]=1.0
    for x in range(1, i+1):
        for y in range(1,j+1):
            slownik[(x,y)] = 0.5 * (slownik[(x-1,y)]+slownik[(x,y-1)])

    return slownik.get((i,j))


def rekursja(i, j):
    if (i<0 or j<0):
        raise ValueError
    elif (i>0 and j>0):
        a=0.5*(rekursja(i-1,j)+rekursja(i,j-1))
        return a
    elif (i!=0 and j==0):
        a=0.0
        return a
    elif (i==0 and j!=0):
        a=1.0
        return a
    elif (i==0 and j==0):
        a=0.5
        return a
    else:
        raise ValueError



class Test(unittest.TestCase):

    def test_wynik(self):
        self.assertEqual(rekursja(1, 2), 0.75)
        self.assertEqual(dynamiczny(1, 2), 0.75)

    def test_bad(self):
        with self.assertRaises(ValueError):
            rekursja(-1, -1)

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()
