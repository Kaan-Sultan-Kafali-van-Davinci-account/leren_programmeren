import fruitmand, random

aantal = ""

while type(aantal) != int:
    try: aantal = int(input("Hoeveel fruiten wil je? ")); break
    except: print("Dat is niet een getal!")

for fruit in range(aantal): print(fruitmand.fruitmand[random.randrange(0, len(fruitmand.fruitmand))]["name"])