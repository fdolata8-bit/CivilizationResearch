class BazaWiedzy:
    def __init__(self):
        self.wynalazki = []

    def dodaj_wynalazek(self, nazwa):
        self.wynalazki.append(nazwa)
        print("NOWY WYNALAZEK:", nazwa)

    def pokaz_wynalazki(self):
        print("Baza wiedzy:")
        for wynalazek in self.wynalazki:
            print("-", wynalazek)
