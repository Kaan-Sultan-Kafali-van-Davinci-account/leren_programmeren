import fruitmand

fruitmand.fruitmand.remove(fruitmand.fruitmand[5])

reoccuring = []

for fruit in fruitmand.fruitmand:
    if not fruit["color"] in reoccuring:
        print(fruit["name"])
        reoccuring.append(fruit["color"])