import fruitmand

for fruit in fruitmand.fruitmand:
    print(fruit["name"], fruit["weight"])

fruitmand.fruitmand.append({
    'name' : 'kerstman meloen',
    'weight' : 1950,
    'color' : 'green',
    'type': 'melon',
    'round' : False
})

totaal_gewicht = 0

for fruit in fruitmand.fruitmand:
    print(fruit["name"], fruit["weight"])
    totaal_gewicht += fruit["weight"]

print("Totaal gewicht van de fruitmand is", totaal_gewicht)