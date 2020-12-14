import random
import math


def calc_pi(n=100):
    j=n
    i=0
    while(j>0):
        a=random.random()
        b=random.random()
        c=(((a)**2)+((b)**2))
        if (c<1):
            i=i+1
        j=j-1
    p=i/n
    Pi=p*4
    return (Pi)

print(calc_pi())

