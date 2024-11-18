import fruitmand

fruitmand.fruitmand = sorted(fruitmand.fruitmand, key=lambda x: len(x["name"]), reverse=True)

vertaling = {"pink": "roze"}

print("De \"" + fruitmand.fruitmand[0]["name"] + "\" (" + str(len(fruitmand.fruitmand[0]["name"])) + " letters) heeft een " + vertaling[fruitmand.fruitmand[0]["color"]] + " kleur en een gewicht van " + str(fruitmand.fruitmand[0]["weight"]) + " gram.")