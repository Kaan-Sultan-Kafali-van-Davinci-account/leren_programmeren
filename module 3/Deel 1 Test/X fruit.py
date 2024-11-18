import fruitmand, random

aantal = int(input("Hoeveel fruiten wil je? "))

for fruit in range(aantal): print(fruitmand.fruitmand[random.randrange(0, len(fruitmand.fruitmand))]["name"])