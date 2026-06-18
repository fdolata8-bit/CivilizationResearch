import random

class Agent:
    def __init__(self, typ="human"):
        self.typ = typ
        self.inteligencja = random.uniform(0.05, 0.2)
        self.inspiracja = random.uniform(0.0, 1.0)
        self.energia_pomyslu = random.uniform(0.0, 1.0)
        self.zyje = True

    def krok(self):
        if not self.zyje:
            return None

        # rozwój
        self.inteligencja += 0.001

        # generowanie idei
        if random.random() < self.inteligencja * self.energia_pomyslu:
            return self.generuj_idee()

        return None

    def generuj_idee(self):
        idee = [
            "ruch", "energia", "informacja",
            "materia", "transport", "praca",
            "ogrzewanie", "ochrona"
        ]

        return random.choice(idee)
