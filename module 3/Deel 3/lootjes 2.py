import random

personen = []

while True:
    naam = input("Vul naam in: ").lower()
    if naam in personen:
        print("Deze heb je al ingevuld.")
    else: personen.append(naam)
    if len(personen) >= 3:
        extra = input("Wil je nog een naam toevoegen? (j/n) ").lower()
        if extra == "n": break
        
personen2 = personen.copy()

succes = False
while not succes:
    random.shuffle(personen); random.shuffle(personen2)
    lootjes = dict(zip(personen, personen2))
    iterations = 0
    for lootje in lootjes:
        if lootjes[lootje] != lootje: iterations += 1
    if iterations == len(personen): succes = True

while True:
    naam = input("Wie wil je zien? (typ 'verlaat' om te verlaten) ").lower()
    if naam == "verlaat": break
    elif naam in personen:
        print(lootjes[naam])
    else: print("Die persoon bestaat niet.")