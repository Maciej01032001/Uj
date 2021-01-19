import ast
import json

def Dodaj_film():

    print("Podaj tytul")
    tytul=input()
    print("Podaj rezysera")
    rezyser=input()
    print("Podaj rok")
    rok=int(input())
    print("Podaj czas")
    czas=int(input())
    print("Podaj kraj")
    kraj=input()
    dictionary[tytul]=[rezyser,rok,czas,kraj]
    test= open("test.txt","w")
    json.dump(dictionary,test)
    test.close()
    return 0

def Wyswietl_po_kraju():
    kraj="Stany Zjednoczone"
    print("Filmy nakrecone w", kraj,"to:")
    for x in dictionary:
        lista=dictionary[x]
        if (lista[3]==kraj):
            print(x)
    return 0

def Wyswietl_po_roku():
    rok=2009
    print("Filmy nakrecone w", rok,"to:")
    for x in dictionary:
        lista=dictionary[x]
        if (lista[1]==rok):
            print(x)
    return 0

def Wyswietl_po_rezyserze():
    rezyser="Quentin Tarantino"
    print("Filmy nakrecone przez", rezyser,"to:")
    for x in dictionary:
        lista=dictionary[x]
        if (lista[0]==rezyser):
            print(x)
    return 0

def Wyswietl_po_czasie():
    czas=100
    print("Filmy dluzsze niz", czas,"to:")
    for x in dictionary:
        lista=dictionary[x]
        if (lista[2]>czas):
            print(x)
    return 0


file = open("test.txt","r")

contents = file.read()
dictionary = ast.literal_eval(contents)


file.close()
print(dictionary["Django"])
print(dictionary["Matrix"])
Wyswietl_po_kraju()
Wyswietl_po_roku()
Wyswietl_po_rezyserze()
Wyswietl_po_czasie()