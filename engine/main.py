from agent import Agent
from swiat import Swiat


swiat = Swiat()

adam = Agent("Adam")
ewa = Agent("Ewa")

swiat.dodaj_agenta(adam)
swiat.dodaj_agenta(ewa)

for _ in range(10):
    swiat.wykonaj_ture()

swiat.baza_wiedzy.pokaz_wynalazki()
print("\n=== WYNALAZKI / ODKRYCIA ===")
print(swiat)
