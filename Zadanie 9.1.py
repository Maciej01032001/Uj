class Node:
    """Klasa reprezentująca węzeł listy jednokierunkowej."""

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)   # bardzo ogólnie
class SingleList:
    """Klasa reprezentująca całą listę jednokierunkową."""

    def __init__(self):
        self.length = 0   # nie trzeba obliczać za każdym razem
        self.head = None
        self.tail = None

    def is_empty(self):
        #return self.length == 0
        return self.head is None

    def count(self):   # tworzymy interfejs do odczytu
        return self.length

    def insert_head(self, node):
        if self.head:   # dajemy na koniec listy
            node.next = self.head
            self.head = node
        else:   # pusta lista
            self.head = self.tail = node
        self.length += 1

    def insert_tail(self, node):   # klasy O(n)
        if self.head:   # dajemy na koniec listy
            self.tail.next = node
            self.tail = node
        else:   # pusta lista
            self.head = self.tail = node
        self.length += 1

    def remove_head(self):          # klasy O(1)
        if self.is_empty():
            raise ValueError("pusta lista")
        node = self.head
        if self.head == self.tail:   # self.length == 1
            self.head = self.tail = None
        else:
            self.head = self.head.next
        node.next = None   # czyszczenie łącza
        self.length -= 1
        return node   # zwracamy usuwany node

    def remove_tail(self):
        if self.is_empty():
            raise ValueError("pusta lista")
        node = self.head
        if self.tail == self.head:  # self.length == 1
            self.tail = self.head = None
        else:
            while(node.next!=self.tail):
                node=node.next
        self.tail=node
        node.next = None  # czyszczenie łącza
        self.length -= 1
        return self
        

    # Zwraca cały węzeł, skraca listę.
    # Dla pustej listy rzuca wyjątek ValueError.

    def merge(self, other):
        while not other.is_empty():
            node=other.head
            self.insert_tail(node)
            node=node.next
            other.remove_head()

    # Węzły z listy other są przepinane do listy self na jej koniec.
    # Po zakończeniu operacji lista other ma być pusta.

    def clear(self):
        while not self.is_empty():
            self.remove_head()# czyszczenie listy

alist = SingleList()
alist.insert_head(Node(11))         # [11]
alist.insert_head(Node(22))         # [22, 11]
alist.insert_tail(Node(33))
alist.remove_tail() #usuwa 33
print ( "alist length {}".format(alist.length) ) # odczyt atrybutu
print ( "alist length {}".format(alist.count()) ) # wykorzystujemy interfejs


blist = SingleList()
blist.insert_head(Node(11))         # nowa lista
blist.insert_head(Node(22))
blist.insert_tail(Node(33))


alist.merge(blist)
print ( "alist length po merge {}".format(alist.count()) )
while not alist.is_empty():   # kolejność 22, 11, 33
    print ( "Czesc alist {}".format(alist.remove_head()) )

print ( "blist length po merge {}".format(blist.length) )
print ( "blsit length po merge {}".format(blist.count()) )


alist.clear()
print ( "alist length po clear {}".format(alist.length) )
while not alist.is_empty():   # kolejność 22, 11, 33
    print ( "remove head {}".format(alist.remove_head()) )
