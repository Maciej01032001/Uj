import random
import math


def random_list_a(N):
    i=0
    list=N * [None]
    while (i!=N):
        list[i]=random.randrange(N)
        i=i+1
    return list

def random_list_b(N):
    i=0
    list=N * [None]
    while (i!=N):
        list[i]=random.randrange(i-5,i+5)
        i=i+1
    return list

def random_list_c(N):
    i=0
    list=N * [None]
    while (i!=N):
        list[i]=random.randrange(i-5,i+5)
        i=i+1
    return reversed(list)


def random_list_d(N):
    i=0
    list=N * [None]
    while (i!=N):
        list[i]=random.gauss(N,2)
        i=i+1
    return list

def random_list_e(N):
    i=0
    list=N * [None]
    while (i!=N):
        list[i]=random.randrange(0,round(math.sqrt(N)))
        i=i+1
    return list


def wypisywanie(a):
    for x in range(len(a)):
        print(a[x])





