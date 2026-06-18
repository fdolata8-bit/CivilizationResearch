import random

class Swiat:
    def __init__(self):
        self.wynalazki = []
        self.historia = []

    def krok(self, agent):
        agent.rozwoj()

        if random.random() < agent.inteligencja:
            self.nowy_wynalazek()

    def nowy_wynalazek(self):
        lista = [
            ("Ogień", "kontrola ognia"),
            ("Koło", "transport"),
            ("Pismo", "zapis informacji"),
            ("Rolnictwo", "produkcja jedzenia"),
            ("Narzędzia kamienne", "pierwsze narzędzia"),
            ("Metalurgia", "obróbka metalu"),
        ]

        w = random.choice(lista)

        if w not in self.wynalazki:
            self.wynalazki.append(w)
            self.historia.append(f"{w[0]} - {w[1]}")
            print(f"🧠 NOWY WYNALAZEK: {w[0]} - {w[1]}")
