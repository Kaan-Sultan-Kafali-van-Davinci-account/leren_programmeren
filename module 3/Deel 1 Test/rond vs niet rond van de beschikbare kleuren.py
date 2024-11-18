import fruitmand

kleuren = ["black", "brown", "dark red", "red", "orange", "yellow", "light green", "green", "dark green", "blue", "purple", "pink", "white"]
kleur = ""

while not kleur in kleuren:
    kleur = input("Kies een kleur: ").lower()
    if not kleur in kleuren:
        print("Kleur niet beschikbaar. Kies een andere kleur.")

round = 0
non_round = 0
for fruit in fruitmand.fruitmand:
    if fruit["color"] == kleur:
        if fruit["round"]:
            round += 1
        else:
            non_round += 1

print("There are", round, "round", kleur, "fruits")
print("There are", non_round, "non-round", kleur, "fruits")
if round > non_round: print("There are more", round - non_round, "round fruits than non-round fruits in the color", str(kleur) + ".")
if non_round > round: print("There are more", non_round - round, "fruits than round fruits in the color", str(kleur) + ".")
if non_round == round: print("There are", round, "round fruits and ", non_round, "non-round fruits in the color", str(kleur) + ".")