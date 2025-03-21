class Produkt:
    def __init__(self, nazwa, cena, ilosc_na_stanie, kategoria):
        self.nazwa = nazwa
        self.cena = cena
        self.ilosc_na_stanie = ilosc_na_stanie
        self.kategoria = kategoria
        self.__kod_kreskowy = None

    def ustaw_kod_kreskowy(self, kod):
        self.__kod_kreskowy = kod

    def pobierz_kod_kreskowy(self):
        return self.__kod_kreskowy

    def oblicz_wartosc(self):
        return self.cena * self.ilosc_na_stanie


class Koszyk:
    koszyki_count = 0

    def __init__(self):
        Koszyk.koszyki_count += 1
        self.numer = Koszyk.koszyki_count
        self.produkty = []
        self.suma = 0

    def dodaj_produkt(self, produkt, ilosc=1):
        if produkt.ilosc_na_stanie >= ilosc:
            for _ in range(ilosc):
                self.produkty.append(produkt)
            produkt.ilosc_na_stanie -= ilosc
            self.suma += produkt.cena * ilosc
            return True

        return False

    def usun_produkt(self, produkt, ilosc=1):
        usunieto = 0
        # pylint: disable=C0200
        for i in range(len(self.produkty)):
            if self.produkty[i] == produkt and usunieto < ilosc:
                self.produkty.pop(i)
                usunieto += 1
                produkt.ilosc_na_stanie += 1
                self.suma -= produkt.cena
        return usunieto


class Supermarket:
    def __init__(self, nazwa, adres):
        self.nazwa = nazwa
        self.adres = adres
        self.produkty = {}
        self.utarg = 0

    def dodaj_produkt(self, produkt, ilosc=1):
        if produkt in self.produkty:
            self.produkty[produkt] += ilosc
        else:
            self.produkty[produkt] = ilosc

    def sprzedaj(self, koszyk):
        self.utarg = self.utarg + koszyk.suma
        print(f"Zakupy w sklepie {self.nazwa} na kwotę {koszyk.suma} zł")
        length = len(koszyk.produkty)
        koszyk.produkty = []
        koszyk.suma = 0
        return length
