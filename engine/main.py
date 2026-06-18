from agent import Agent
from swiat import Swiat

swiat = Swiat()
agent = Agent()

print("🚀 START CYWILIZACJI\n")

for i in range(200):
    swiat.krok(agent)

print("\n🌍 KONIEC SYMULACJI\n")

print("🧠 WYNALAZKI:")
for i, w in enumerate(swiat.wynalazki, 1):
    print(f"{i}. {w[0]} — {w[1]}")

print("\n📜 HISTORIA CYWILIZACJI:\n")
for h in swiat.historia:
    print("•", h)
