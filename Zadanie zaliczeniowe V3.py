import json

class Database:


    def Meni(self):
        print("\nDodaj film (0), Usun film (1), Znajdz film (2), Wypisz alfabetycznie (3), Wypisz wedlug premiery (4),\n"
              "Wyswietl filmy z danych lat (5), Wyswietl filmy danego rezysera (6), Zakoncz dzialanie (7)" )
        answer=8
        while (answer!="7"):
            print("Wybierz jedno z polecen")
            answer = input()
            if (answer=="0"):
                Database.Dodaj_film(self)
            if (answer=="1"):
                Database.Usun_film(self)
            if (answer=="2"):
                Database.Znajdz_film(self)
            if (answer=="3"):
                Database.Wypisz_alfabetycznie(self)
            if (answer=="4"):
                Database.Wypisz_po_roku(self)
            if (answer == "6"):
                Database.Wyswietl_po_rezyserze(self)
            if (answer == "5"):
                Database.Wyswietl_po_roku(self)
            if (answer == "7"):
                return 0

    def Dodaj_film(self):

        print("Podaj tytul")
        tytul=input()
        print("Podaj rezysera")
        rezyser=input()
        print("Podaj rok")
        rok=int(input())
        dictionary[tytul]=[rezyser,rok]
        with open('test.txt','w') as outfile:
            json.dump(dictionary, outfile)
        return 0

    def Usun_film(self):
        print("Podaj tytul")
        tytul = input()
        if (tytul in dictionary):
            dictionary.pop(tytul)
            with open('test.txt', 'w') as outfile:
                json.dump(dictionary, outfile)
        else:
            print("Nie ma takiego filmu")

    def Znajdz_film(self):
        print("Podaj tytul")
        tytul = input()
        if (tytul in dictionary):
            print(tytul,dictionary[tytul][0],dictionary[tytul][1])
        else:
            print("Nie ma takeigo filmu")

    def Wyswietl_po_roku(self):
        print("Z jakich lat interesuja cie filmy ?")
        print("Od:")
        rok=int(input())
        print("Do:")
        rok_2=int(input())
        print("Filmy nakrecone po", rok,"ale przed",rok_2,"to:")
        lista_2=[]
        for x in dictionary:
            lista=dictionary[x]
            if (lista[1]>=rok and lista[1]<=rok_2):
                lista_2.append([x,dictionary[x][1]])
        lista_2.sort(key = lambda x: x[1])
        for y in lista_2:
            print(y[1],y[0].ljust(30))
        return 0

    def Wyswietl_po_rezyserze(self):
        print("Filmy jakiego rezysera cie interesuja ?")
        rezyser=input()
        a=0
        for x in dictionary:
            lista=dictionary[x]
            if (lista[0]==rezyser):
                a=a+1
        if (a!=0):
            print("Filmy nakrecone przez", rezyser,"to:")
            for x in dictionary:
                lista=dictionary[x]
                if (lista[0]==rezyser):
                    print(x.ljust(30),dictionary[x][1])
        else:
            print("Nie ma takiego rezysera")
        return 0

    def Wypisz_alfabetycznie(self):
        lista=[]
        for x in dictionary:
            lista.append(x)
        lista.sort()
        for x in lista:
            print(x.ljust(30),dictionary[x][0].ljust(20),dictionary[x][1])

    def Wypisz_po_roku(self):
        lista=[]
        for x in dictionary:
            lista.append([x,dictionary[x][1]])
        lista.sort(key = lambda x: x[1])
        for x in lista:
            print(x[1],x[0].ljust(30),dictionary[x[0]][0].ljust(20))




with open('test.txt') as f:
  dictionary = json.load(f)


Database.Meni(dictionary)
