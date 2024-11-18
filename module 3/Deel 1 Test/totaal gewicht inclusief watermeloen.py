import fruitmand

for fruit in fruitmand.fruitmand: print(fruit["name"], fruit["weight"])

fruitmand.fruitmand.append({
    'name' : 'watermeloen',
    'weight' : 2000,
    'color' : 'green',
    'type': 'melon',
    'round' : True
})

for fruit in fruitmand.fruitmand: print(fruit["name"], fruit["weight"])