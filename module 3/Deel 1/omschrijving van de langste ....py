import fruitmand

fruitmand.fruitmand = sorted(fruitmand.fruitmand, key=lambda x: len(x["name"]), reverse=True)

vertaling = {"orange": "oranje"}

print("De \"" + fruitmand.fruitmand[0]["name"] + "\" (" + str(len(fruitmand.fruitmand[0]["name"])) + " letters) heeft een " + vertaling[fruitmand.fruitmand[0]["color"]] + " kleur, het is van een " + fruitmand.fruitmand[0]["type"] + " soort en een gewicht van " + str(fruitmand.fruitmand[0]["weight"]) + " gram.")