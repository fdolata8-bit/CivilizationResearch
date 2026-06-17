import random


class Agent:
    def __init__(self, imie):
        self.imie = imie
        self.iq = random.randint(80, 140)
        self.wiedza = 0
        self.ciekawosc = random.randint(1, 100)

    def ucz_sie(self):
        przyrost = max(1, self.iq // 50)
        self.wiedza += przyrost

        print(
            self.imie,
            "IQ:",
            self.iq,
            "Wiedza:",
            self.wiedza
        )

    def czy_odkryl_cos(self):
        szansa = self.ciekawosc + (self.iq // 2)

        if random.randint(1, 1000) < szansa:
            return True

        return False
