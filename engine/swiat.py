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

            if agent.czy_odkryl_cos():
                nazwa = f"Odkrycie_{self.tura}_{agent.imie}"
                self.baza_wiedzy.dodaj_wynalazek(nazwa)
