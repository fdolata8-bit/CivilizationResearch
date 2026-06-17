import random

class Swiat:
    def __init__(self):
        self.wynalazki = []

    def krok(self, agent):
        # agent się rozwija
        agent.rozwoj()

        # szansa na wynalazek
        if random.random() < agent.inteligencja:
            self.nowy_wynalazek()

    def nowy_wynalazek(self):
        mozliwe = [
            "Ogień",
            "Koło",
            "Pismo",
            "Rolnictwo",
            "Narzędzia kamienne"
        ]

        w = random.choice(mozliwe)

        if w not in self.wynalazki:
            self.wynalazki.append(w)
            print("🧠 Wynalazek:", w)
