import fruitmand

fruitmand.fruitmand.remove(fruitmand.fruitmand[5])

reoccuring = {
    "black": False,
    "brown": False,
    "dark red": False,
    "red": False,
    "orange": False,
    "yellow": False,
    "light green": False,
    "green": False,
    "dark green": False,
    "blue": False,
    "purple": False,
    "pink": False,
    "white": False
}

for fruit in fruitmand.fruitmand:
    if not reoccuring[fruit["color"]]:
        print(fruit["name"])
        reoccuring[fruit["color"]] = True