import random

soorten = ("Harten", "Klaveren", "Scheppen", "Ruiten"); waarden = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "Boer", "Vrouw", "Heer", "Aas")
deck = [f"{waarde} van {soort}" for soort in soorten for waarde in waarden] + ["Joker 1", "Joker 2"]

random.shuffle(deck)
print("De bovenste 7 kaarten zijn: ")
for x in range(7): print(deck.pop(0))
print(f"Overgebleven deck (aantal {len(deck)}):", deck)