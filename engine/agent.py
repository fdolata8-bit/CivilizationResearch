class Agent:
    def __init__(self, imie):
        self.imie = imie
        self.iq = 100
        self.wiedza = 0
        self.ciekawosc = 50

    def ucz_sie(self):
        self.wiedza += 1
        print(self.imie, "uczy się. Wiedza:", self.wiedza)
