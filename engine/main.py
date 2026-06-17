from agent import Agent
from swiat import Swiat

swiat = Swiat()
agent = Agent()

print("🚀 START CYWILIZACJI")

for i in range(200):
    swiat.krok(agent)

print("\n🌍 KONIEC")
print("Wynalazki:")

for w in swiat.wynalazki:
    print("-", w)
