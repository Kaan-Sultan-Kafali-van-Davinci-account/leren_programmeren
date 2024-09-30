try: total_small = int(input("Hoeveel pizza small wil je bestellen? "))
except: total_small = 0; print("Small was niet een heel getal, dus het is beschouwd als 0")
try: total_medium = int(input("Hoeveel pizza medium wil je bestellen? "))
except: total_medium = 0; print("Medium was niet een heel getal, dus het is beschouwd als 0")
try: total_large = int(input("Hoeveel pizza large wil je bestellen? "))
except: total_large = 0; print("Large was niet een heel getal, dus het is beschouwd als 0")

pizza_small = 6.50
pizza_medium = 9.30
pizza_large = 11.10

small_total = pizza_small * total_small
medium_total = pizza_medium * total_medium
large_total = pizza_large * total_large

print("---------------- Bon -----------------")
if total_small: print("Small Prijs: €" + str(small_total))
if total_medium: print("Medium Prijs: €" + str(medium_total))
if total_large: print("Large Prijs: €" + str(large_total))
print("--------------------------------------")