class biblioteka():
    def __init__(self, nazwa_biblioteki="Moja Biblioteka"):
        self.nazwa_biblioteki = nazwa_biblioteki
        self.ksiazki = []
        self.czytelnicy = {}
        self.ID = 0

    def Dodaj_ksiazke(self, tytul, autor, rok_wydania):
        self.ID += 1
        nowa_ksiazka = {'id': self.ID, 'tytul': tytul, 'autor': autor,
                        'rok_wydania': rok_wydania, 'wypozyczona': False,
                        'czytelnik': None}
        self.ksiazki.append(nowa_ksiazka)
        return self.ID

    def UsunKsiazke(self, id_ksiazki):
        for ksiazka in self.ksiazki:
            if ksiazka['id'] == id_ksiazki:
                self.ksiazki.remove(ksiazka)
                return True
        return False

    def znajdz_ksiazke(self, fraza):
        wyniki = []
        for ksiazka in self.ksiazki:
            if (fraza.lower() in ksiazka['tytul'].lower()
                    or fraza.lower() in ksiazka['autor'].lower()):
                wyniki.append(ksiazka)
        return wyniki

    def wypozycz(self, id_ksiazki, czytelnik_id):
        for i in range(0, len(self.ksiazki)):
            if self.ksiazki[i]['id'] == id_ksiazki:
                if not self.ksiazki[i]['wypozyczona']:
                    self.ksiazki[i]['wypozyczona'] = True
                    self.ksiazki[i]['czytelnik'] = czytelnik_id
                    return True
                else:
                    return False
        return False

    def oddaj(self, id_ksiazki):
        for ksiazka in self.ksiazki:
            if ksiazka['id'] == id_ksiazki and ksiazka['wypozyczona']:
                ksiazka['wypozyczona'] = False
                ksiazka['czytelnik'] = None
                return True
        return False

    def lista_ksiazek(self):
        if (len(self.ksiazki) == 0):
            print("Brak książek w bibliotece")
            return []
        else:
            return self.ksiazki

    def dodaj_czytelnika(self, imie, nazwisko, adres):
        czytelnik_id = len(self.czytelnicy) + 1
        self.czytelnicy[czytelnik_id] = {'imie': imie, 'nazwisko': nazwisko,
                                         'adres': adres}
        return czytelnik_id

    def info(self):
        print(f"Biblioteka: {self.nazwa_biblioteki}")
        print(f"Liczba książek: {len(self.ksiazki)}")
        print(f"Liczba czytelników: {len(self.czytelnicy)}")
