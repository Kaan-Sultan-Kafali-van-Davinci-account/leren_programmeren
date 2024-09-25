if {"j": True, "n": False}[input("Is de kaas geel? j/n ").lower()]:
  if {"j": True, "n": False}[input("Zitten er gaten in? j/n ").lower()]: print("Emmenthaler") if {"j": True, "n": False}[input("Is de kaas belachelijk duur? j/n ").lower()] else print("Leerdammer")
  else: print("Parmigiano Reggiano") if {"j": True, "n": False}[input("Is de kaas hard als steen? j/n ").lower()] else print("Goudse Kaas")
else:
  if {"j": True, "n": False}[input("Heeft de kaas blauwe schimmel? j/n ").lower()]: print("Blue de Rochbaron") if {"j": True, "n": False}[input("Heeft de kaas korst? j/n ").lower()] else print("Foume d'Ambert")
  else: print("Camembert") if {"j": True, "n": False}[input("Heeft de kaas korst? j/n ").lower()] else print("Mozzarella")