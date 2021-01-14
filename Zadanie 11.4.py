import random
import time

def random_list_a(N):
    i=0
    list=N * [None]
    while (i!=N):
        list[i]=random.randrange(N)
        i=i+1
    return list



a=random_list_a(10**2)
b=random_list_a(10**3)
c=random_list_a(10**4)
d=random_list_a(10**5)
e=random_list_a(10**6)


def swap(L, left, right):
    """Zamiana miejscami dwóch elementów."""
    # L[left], L[right] = L[right], L[left]
    item = L[left]
    L[left] = L[right]
    L[right] = item


def selectsort(L, left, right):
    for i in range(left, right):
        k = i
        for j in range(i+1, right+1):
            if L[j] < L[k]:
                k = j
        item = L[k]
        while k > i:
            L[k] = L[k-1]
            k = k-1
        L[i] = item
    return L

def selectsort_time(L, left, right):
    start_time = time.time()
    for i in range(left, right):
        k = i
        for j in range(i+1, right+1):
            if L[j] < L[k]:
                k = j
        item = L[k]
        while k > i:
            L[k] = L[k-1]
            k = k-1
        L[i] = item
    return (time.time() - start_time)

def insertsort(L, left, right):
    for i in range(right, left, -1):   # ustawiam wartownika
        if L[i-1] > L[i]:
            swap(L, i-1, i)
    for i in range(left+2, right+1):
        j = i
        item = L[i]
        while item < L[j-1]:   # robimy miejsce na item
            L[j] = L[j-1]
            j = j-1
        L[j] = item
    return L

def insertsort_time(L, left, right):
    start_time = time.time()
    for i in range(right, left, -1):   # ustawiam wartownika
        if L[i-1] > L[i]:
            swap(L, i-1, i)
    for i in range(left+2, right+1):
        j = i
        item = L[i]
        while item < L[j-1]:   # robimy miejsce na item
            L[j] = L[j-1]
            j = j-1
        L[j] = item
    return (time.time() - start_time)

def bubblesort(L, left, right):
    limit = right
    while True:
        k = left-1   # lewy wskaźnik przestawianej pary
        for i in range(left, limit):
            if L[i] > L[i+1]:
                swap(L, i, i+1)
                k = i
        if k > left:
            limit = k
        else:
            break

def bubblesort_time(L, left, right):
    start_time = time.time()
    limit = right
    while True:
        k = left-1   # lewy wskaźnik przestawianej pary
        for i in range(left, limit):
            if L[i] > L[i+1]:
                swap(L, i, i+1)
                k = i
        if k > left:
            limit = k
        else:
            break
    return (time.time() - start_time)

def shakersort(L, left, right):
    k = right
    while left < right:
        for j in range(right, left, -1):   # od prawej
            if L[j-1] > L[j]:
                swap(L, j-1, j)
                k = j
        left = k
        for j in range(left, right):   # od lewej
            if L[j] > L[j+1]:
                swap(L, j, j+1)
                k = j
        right = k

def shakersort_time(L, left, right):
    start_time = time.time()
    k = right
    while left < right:
        for j in range(right, left, -1):   # od prawej
            if L[j-1] > L[j]:
                swap(L, j-1, j)
                k = j
        left = k
        for j in range(left, right):   # od lewej
            if L[j] > L[j+1]:
                swap(L, j, j+1)
                k = j
        right = k
    return (time.time() - start_time)

def shellsort_time(L, left, right):
    start_time = time.time()
    h = (right - left) // 2
    while h > 0:
        for i in range(left + h, right + 1):
            for j in range(i, left + h - 1, -h):
                if L[j - h] > L[j]:
                    swap(L, j - h, j)
        h = h // 2
    return (time.time() - start_time)

def quicksort(L, left, right):
    if left >= right:
        return
    swap(L, left, (left + right) // 2)   # element podziału
    pivot = left                      # przesuń do L[left]
    for i in range(left + 1, right + 1):   # podział
        if L[i] < L[left]:
            pivot += 1
            swap(L, pivot, i)
    swap(L, left, pivot)     # odtwórz element podziału
    quicksort(L, left, pivot - 1)
    quicksort(L, pivot + 1, right)


def quicksort_time(L, left, right):
    start_time = time.time()
    if left >= right:
        return
    swap(L, left, (left + right) // 2)   # element podziału
    pivot = left                      # przesuń do L[left]
    for i in range(left + 1, right + 1):   # podział
        if L[i] < L[left]:
            pivot += 1
            swap(L, pivot, i)
    swap(L, left, pivot)     # odtwórz element podziału
    quicksort(L, left, pivot - 1)
    quicksort(L, pivot + 1, right)
    return (time.time() - start_time)








def clocker(L,left,right):
    print("Czasy wykonania dla poszczegolnych funkcji to ")
    print("Selectsort: ")
    print(selectsort_time(L,left,right))
    print("Insertsort: ")
    print(insertsort_time(L,left,right))
    print("Bubblesort: ")
    print(bubblesort_time(L,left,right))
    print("Shakersort: ")
    print(shakersort_time(L,left,right))
    print("Shellsort: ")
    print(shellsort_time(L,left,right))
    print("Quicksort: ")
    print(quicksort_time(L,left,right))

def clocker_wydajniejszy(L,left,right):
    print("Czasy wykonania dla poszczegolnych funkcji to ")
    print("Insertsort: ")
    print(insertsort_time(L,left,right))
    print("Bubblesort: ")
    print(bubblesort_time(L,left,right))
    print("Shakersort: ")
    print(shakersort_time(L,left,right))
    print("Quicksort: ")
    print(quicksort_time(L,left,right))

clocker(a,0,99)
clocker(b,0,999)
clocker(c,0,9999)
clocker_wydajniejszy(d,0,99999)
clocker_wydajniejszy(e,0,999999)
