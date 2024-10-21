import random
kleuren = ("oranje", "blauw", "groen", "bruin")
zak = []
aantal = int(input("Hoeveel M&M's moet er toegevoegd moeten worden? "))
for i in range(aantal): zak.append(random.choice(kleuren))
print("De inhoud van de zak is: ")
print(zak)