import time
from agent import Agent
from swiat import Swiat

swiat = Swiat()

agenci = [
    Agent("scholar"),
    Agent("farmer"),
    Agent("warrior")
]

print("🚀 CYWILIZACJA URUCHOMIONA - TRYB CIĄGŁY\n")

tick = 0

while True:
    tick += 1

    for agent in agenci:
        swiat.krok(agent)

    # co jakiś czas pokazuj status
    if tick % 20 == 0:
        print(f"\n⏳ Tura: {tick}")
        print(f"🧠 Wynalazki: {len(swiat.wynalazki)}")

    time.sleep(0.1)  # spowalnia żebyś widział rozwój
