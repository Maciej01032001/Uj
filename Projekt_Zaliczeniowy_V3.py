import json

class Database:

    with open('test.txt') as f:
        dictionary = json.load(f)

    def Meni(self):
        print("\nDodaj film (0), Usun film (1), Znajdz film (2),\n" 
              "Wypisz alfabetycznie (3), Wypisz wedlug premiery (4),\n"
              "Wyswietl filmy z danych lat (5), Wyswietl filmy danego rezysera (6),\n"
              "Zakoncz dzialanie (7)" )
        answer=8
        while (answer!="7"):
            print("Wybierz jedno z polecen:")
            answer = input()
            if (answer=="0"):
                self.Dodaj_film()
                print("\nDodaj film (0), Usun film (1), Znajdz film (2),\n"
                      "Wypisz alfabetycznie (3), Wypisz wedlug premiery (4),\n"
                      "Wyswietl filmy z danych lat (5), Wyswietl filmy danego rezysera (6),\n"
                      "Zakoncz dzialanie (7)")
            if (answer=="1"):
                self.Usun_film()
                print("\nDodaj film (0), Usun film (1), Znajdz film (2),\n"
                      "Wypisz alfabetycznie (3), Wypisz wedlug premiery (4),\n"
                      "Wyswietl filmy z danych lat (5), Wyswietl filmy danego rezysera (6),\n"
                      "Zakoncz dzialanie (7)")
            if (answer=="2"):
                self.Znajdz_film()
                print("\nDodaj film (0), Usun film (1), Znajdz film (2),\n"
                      "Wypisz alfabetycznie (3), Wypisz wedlug premiery (4),\n"
                      "Wyswietl filmy z danych lat (5), Wyswietl filmy danego rezysera (6),\n"
                      "Zakoncz dzialanie (7)")
            if (answer=="3"):
                self.Wypisz_alfabetycznie()
                print("\nDodaj film (0), Usun film (1), Znajdz film (2),\n"
                      "Wypisz alfabetycznie (3), Wypisz wedlug premiery (4),\n"
                      "Wyswietl filmy z danych lat (5), Wyswietl filmy danego rezysera (6),\n"
                      "Zakoncz dzialanie (7)")
            if (answer=="4"):
                self.Wypisz_po_roku()
                print("\nDodaj film (0), Usun film (1), Znajdz film (2),\n"
                      "Wypisz alfabetycznie (3), Wypisz wedlug premiery (4),\n"
                      "Wyswietl filmy z danych lat (5), Wyswietl filmy danego rezysera (6),\n"
                      "Zakoncz dzialanie (7)")
            if (answer == "6"):
                self.Wyswietl_po_rezyserze()
                print("\nDodaj film (0), Usun film (1), Znajdz film (2),\n"
                      "Wypisz alfabetycznie (3), Wypisz wedlug premiery (4),\n"
                      "Wyswietl filmy z danych lat (5), Wyswietl filmy danego rezysera (6),\n"
                      "Zakoncz dzialanie (7)")
            if (answer == "5"):
                self.Wyswietl_po_roku()
                print("\nDodaj film (0), Usun film (1), Znajdz film (2),\n"
                      "Wypisz alfabetycznie (3), Wypisz wedlug premiery (4),\n"
                      "Wyswietl filmy z danych lat (5), Wyswietl filmy danego rezysera (6),\n"
                      "Zakoncz dzialanie (7)")
            if (answer == "7"):
                return 0

    def Wypisz_alfabetycznie(self):
        lista = []
        for x in Database.dictionary:
            lista.append(x)
        lista.sort()
        for x in lista:
            print(x.ljust(30), Database.dictionary[x][0].ljust(20), Database.dictionary[x][1])

    def Dodaj_film(self):

        print("Podaj tytul")
        tytul = input()
        print("Podaj rezysera")
        rezyser = input()
        print("Podaj rok")
        rok = int(input())
        Database.dictionary[tytul] = [rezyser, rok]
        with open('test.txt', 'w') as outfile:
            json.dump(Database.dictionary, outfile)
        return 0

    def Usun_film(self):
        print("Podaj tytul")
        tytul = input()
        if (tytul in Database.dictionary):
            Database.dictionary.pop(tytul)
            with open('test.txt', 'w') as outfile:
                json.dump(Database.dictionary, outfile)
        else:
            print("Nie ma takiego filmu")

    def Znajdz_film(self):
        print("Podaj tytul")
        tytul = input()
        a=0
        for x in Database.dictionary:
            tytul_2=x
            if (tytul in tytul_2):
                print(tytul_2,Database.dictionary[tytul_2][0],Database.dictionary[tytul_2][1])
                a=a+1
        if(a==0):
            print("Nie ma takiego filmu")

    def Wyswietl_po_roku(self):
        print("Z jakich lat interesuja cie filmy ?")
        print("Od:")
        rok=int(input())
        print("Do:")
        rok_2=int(input())
        print("Filmy nakrecone po", rok,"ale przed",rok_2,"to:")
        lista_2=[]
        for x in Database.dictionary:
            lista=Database.dictionary[x]
            if (lista[1]>=rok and lista[1]<=rok_2):
                lista_2.append([x,Database.dictionary[x][1]])
        lista_2.sort(key = lambda x: x[1])
        for y in lista_2:
            print(y[1],y[0].ljust(30))
        return 0

    def Wyswietl_po_rezyserze(self):
        print("Filmy jakiego rezysera cie interesuja ?")
        rezyser=input()
        a=0
        nowa=[]
        for x in Database.dictionary:
            lista=Database.dictionary[x]
            if (rezyser in lista[0]):
                nowa.append([x,Database.dictionary[x][1]])
                a=a+1
        nowa.sort(key = lambda x: x[1])
        for y in nowa:
            print(y[1],y[0].ljust(30))
        if (a==0):
            print("Nie ma takiego rezysera")
        return 0



    def Wypisz_po_roku(self):
        lista=[]
        for x in Database.dictionary:
            lista.append([x,Database.dictionary[x][1]])
        lista.sort(key = lambda x: x[1])
        for x in lista:
            print(x[1],x[0].ljust(30),Database.dictionary[x[0]][0].ljust(20))






test=Database()
test.Meni()