v1 = {"j": True, "n": False}[input("Is de kaas geel? j/n ")]
if v1:
  v2 = {"j": True, "n": False}[input("Zitten er gaten in? j/n ")]
  if v2:
    v3 = {"j": True, "n": False}[input("Is de kaas belachelijk duur? j/n ")]
    if v3: print("Emmenthaler")
    else: print("Leerdammer")
  else:
    v3 = {"j": True, "n": False}[input("Is de kaas hard als steen? j/n ")]
    if v3: print("Parmigiano Reggiano")
    else: print("Goudse Kaas")
else:
  v2 = {"j": True, "n": False}[input("Heeft de kaas blauwe schimmel? j/n ")]
  if v2:
    v3 = {"j": True, "n": False}[input("Heeft de kaas korst? j/n ")]
    if v3: print("Blue de Rochbaron")
    else: print("Foume d'Ambert")
  else:
    v3 = {"j": True, "n": False}[input("Heeft de kaas korst? j/n ")]
    if v3: print("Camembert")
    else: print("Mozzarella")