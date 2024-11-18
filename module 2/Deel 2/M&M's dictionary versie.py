import random
kleuren = ("oranje", "blauw", "groen", "bruin")
zak = {}
aantal = int(input("Hoeveel M&M's moet er toegevoegd moeten worden? "))
for i in range(aantal):
    c = random.choice(kleuren)
    if c in zak: zak[c] += 1
    else: zak[c] = 1   
print("De inhoud van de zak is: ")
print(zak)

#"oranje": 0, "blauw": 0, "groen": 0, "bruin": 0