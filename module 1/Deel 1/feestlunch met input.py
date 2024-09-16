criossant = int(input("Hoeveel criossanten, "))
stokbrood = int(input("Hoeveel stokbroden, "))
kortingbonnen = int(input("Hoeveel Kortingbonnen heb je, "))

product_prijzen = {
  "criossant": 0.39,
  "stokbrood": 2.78,
  
  "kortingbonnen": 0.50}

prijs = ((criossant * product_prijzen["criossant"]) + (stokbrood * product_prijzen["stokbrood"])) - (kortingbonnen * product_prijzen["kortingbonnen"])

print(f"Bij de bakker kost alles samen {prijs} als de {kortingbonnen} kortingsbonnen nog geldig zijn")
