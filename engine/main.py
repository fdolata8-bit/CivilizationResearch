from agent import Agent
from swiat import Swiat
import random

# 1000 agentów
agenci = [Agent() for _ in range(1000)]

swiat = Swiat()

print("🚀 START EMERGENTNEJ CYWILIZACJI\n")

for i in range(5000):

    swiat.krok(agenci)

    if i % 200 == 0:
        print(f"⏳ Rok {i} | idee: {len(swiat.idee)} | wynalazki: {len(swiat.wynalazki)}")

print("\n🌍 KONIEC")

print("\n🧠 WYNALEZKI EMERGENTNE:")
for w in swiat.wynalazki:
    print("-", w)
