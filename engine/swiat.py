import random

class Swiat:
    def __init__(self):
        self.rok = 0
        self.idee = []
        self.wynalazki = []

    def krok(self, agenci):
        self.rok += 1

        nowe_idee = []

        # zbieranie idei od agentów
        for agent in agenci:
            idea = agent.krok()
            if idea:
                nowe_idee.append(idea)

        self.idee.extend(nowe_idee)

        # emergencja wynalazków
        if len(self.idee) > 5:
            self.probuj_wynalazek()

    def probuj_wynalazek(self):
        if random.random() < 0.3:
            a = random.choice(self.idee)
            b = random.choice(self.idee)

            if a != b:
                nowy = f"{a} + {b}"

                if nowy not in self.wynalazki:
                    self.wynalazki.append(nowy)
                    print(f"🧠 [{self.rok}] NOWY WYNALAZEK: {nowy}")
