import fruitmand

for fruit in fruitmand.fruitmand: print(fruit["name"], fruit["weight"])

fruitmand.fruitmand.append({
    'name' : 'kerstman meloen',
    'weight' : 1950,
    'color' : 'green',
    'type': 'melon',
    'round' : False
})

for fruit in fruitmand.fruitmand: print(fruit["name"], fruit["weight"])