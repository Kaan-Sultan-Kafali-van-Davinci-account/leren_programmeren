from termcolor import cprint

product_prijzen = {
  "criossant": 0.39,
  "stokbrood": 2.78,
  
  "kortingbonnen": 0.50}

criossant = 17
stokbrood = 2.78

kortingbonnen = 3

prijs = ((criossant * product_prijzen["criossant"]) + (stokbrood * product_prijzen["stokbrood"])) - (kortingbonnen * product_prijzen["kortingbonnen"])

cprint(f"Bij de bakker kost alles samen {prijs} als de {kortingbonnen} kortingsbonnen nog geldig zijn", "blue")





toegang = 7.45

personen = 4

cent_vr = 0.37

vijf_minuten = 9

prijs = (personen * toegang) + ((vijf_minuten * cent_vr) * personen)

cprint(f"Dit geweldige dagje-uit met {personen} mensen in de Speelhal met {vijf_minuten * 5} minuten VR kost je maar {round(prijs, 2)} euro", "green")
