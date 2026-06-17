import random

class Swiat:
    def __init__(self):
        self.rok = 0
        self.wynalazki = []

    def krok(self, agent):
        self.rok += 1

        # rozwój agenta
        agent.rozwoj()

        # szansa na wynalazek
        if random.random() < agent.inteligencja:
            self.nowy_wynalazek()

    def nowy_wynalazek(self):
        lista = [
            ("Ogień", "kontrola ognia"),
            ("Koło", "transport"),
            ("Rolnictwo", "produkcja jedzenia"),
            ("Pismo", "zapis informacji"),
        ]

        w = random.choice(lista)

        if w not in self.wynalazki:
            self.wynalazki.append(w)
            print(f"🧠 WYNALAZEK: {w[0]} - {w[1]}")
