from agent import Agent
from wiedza import BazaWiedzy


class Swiat:
    def __init__(self):
        self.tura = 0
        self.agenci = []
        self.baza_wiedzy = BazaWiedzy()

    def dodaj_agenta(self, agent):
        self.agenci.append(agent)

    def wykonaj_ture(self):
        self.tura += 1

        print("")
        print("=== TURA", self.tura, "===")

        for agent in self.agenci:
            agent.ucz_sie()

        if self.tura == 5:
            self.baza_wiedzy.dodaj_wynalazek("Ogień")
